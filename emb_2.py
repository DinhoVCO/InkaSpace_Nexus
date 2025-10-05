from pathlib import Path
from collections import defaultdict
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
import os
import re
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
import json

load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
USE_SECONDARY_SPLIT = False   
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
HEADERS_TO_SPLIT = [("#", "H1"), ("##", "H2"), ("###", "H3")]                               # Number of results
def split_markdown(text: str):
    doc = Document(page_content=text)
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name="gpt-4",chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        )
    docs = splitter.split_documents([doc])
    return docs


def extract_publication_date(text):
    """
    Busca una línea que comience con '.' y extrae una fecha simple (e.g. '2010 Apr 30' o '2011 May').
    Devuelve la primera coincidencia o None.
    """
    for linea in text.splitlines():
        linea = linea.strip()
        if linea.startswith('.'):
            # Busca una fecha como "2010 Apr 30" o "2011 May"
            match = re.search(r'\b(19|20)\d{2}\s+[A-Za-z]{3}(?:\s*\d{1,2})?', linea)
            if match:
                return match.group(0)
    return None

def extract_publication_date_v2(text):
    """
    Busca una línea que comience con '.' y extrae una fecha simple en formato ISO (YYYY-MM-DD o YYYY-MM).
    Ejemplos de entrada:
        . 2010 Apr 30;...
        . Author manuscript; available in PMC: 2011 May 1.
    Devuelve una cadena 'YYYY-MM-DD', 'YYYY-MM' o None.
    """
    month_map = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }

    for linea in text.splitlines():
        linea = linea.strip()
        if linea.startswith('.'):
            # Buscar fechas como '2010 Apr 30' o '2011 May'
            match = re.search(r'\b(19|20)\d{2}\s+([A-Za-z]{3})(?:\s+(\d{1,2}))?', linea)
            if match:
                year = match.group(0).split()[0]
                month_abbr = match.group(2)
                day = match.group(3)

                month = month_map.get(month_abbr[:3].title())
                if not month:
                    continue

                if day:
                    # Normalizar día
                    day = day.zfill(2)
                    return f"{year}-{month}-{day}"
                else:
                    return f"{year}-{month}"
    return None
    
def extract_metadata_from_md(text: str):
    """Extrae metadatos clave desde un texto Markdown de PubMed/PMC"""
    metadata = {}

    # Title
    titles_n1 = re.findall(r'^# (.+)', text, flags=re.MULTILINE)
    if titles_n1:
        metadata["title"] = titles_n1[0]

     # Recortar texto solo hasta antes de "* Author information"
    pre_authors_section = text.split("* Author information")[0]

    # Authors (solo en la parte anterior a Author information)
    authors = re.findall(r'^###\s+(.+)', pre_authors_section, flags=re.MULTILINE)
    if authors:
        metadata["authors"] = ", ".join(authors)


    # Author information (primer bloque después de ###)
    author_info_match = re.search(r'### .+?\n([\s\S]*?)(?=\nFind articles)', text)
    if author_info_match:
        metadata["author_information"] = author_info_match.group(1).strip()

    # Article notes (línea con Received / Accepted / Issue date)
    notes_match = re.search(r'(Received .*?Issue date.*?\.)', text)
    if notes_match:
        metadata["article_notes"] = notes_match.group(1).strip()

    # Copyright & License
    copyright_match = re.search(r'(Copyright ©.*?Microbiology)', text)
    if copyright_match:
        metadata["copyright_license"] = copyright_match.group(1).strip()

    # PMCID
    pmcid_match = re.search(r'PMCID:\s*(PMC\d+)', text)
    if pmcid_match:
        metadata["pmcid"] = pmcid_match.group(1).strip()

    # PMID
    pmid_match = re.search(r'PMID:\s*\[(\d+)\]', text)
    if pmid_match:
        metadata["pmid"] = pmid_match.group(1).strip()

    # extraer fecha
    date = extract_publication_date_v2(text)
    if date:
        metadata["publication_date"] = date
    return metadata


def process_markdown_directory(in_dir: str, collection: str):
    """Main function to process markdown files and store them into a local Qdrant vector database."""
    
    in_dir = Path(in_dir)

    # 1) Collect & split
    all_docs = []
    counts = defaultdict(int)
    all_metadata = {}
    for md_path in in_dir.rglob("*.md"):
        
        id = os.path.dirname(md_path).split('/')[-1]
        text = md_path.read_text(encoding="utf-8", errors="ignore")
        docs = split_markdown(text)

        metadata =extract_metadata_from_md(text)
        all_metadata[metadata["pmcid"]] = metadata
        for d in docs:
            d.metadata = metadata
        
        all_docs.extend(docs)
        counts[md_path.as_posix()] += len(docs)


    # Guardar en un archivo JSON
    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(all_metadata, f, ensure_ascii=False, indent=4)
    print(f"Collected {len(all_docs)} chunks from {len(counts)} files.")

    # 2) Embeddings
    embeddings = MistralAIEmbeddings(model="mistral-embed")

    # 3) Local embedded Qdrant (persists under qdrant_dir)
    client = QdrantClient(
        url=QDRANT_URL, 
        api_key=QDRANT_API_KEY,
    )

    # 4) Create collection if missing (size must match embedding dim)
    vector_size = len(embeddings.embed_query("sample text"))
    try:
        client.get_collection(collection_name=collection)
    except Exception:
        client.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )

    # 5) Upsert via LangChain QdrantVectorStore
    store = QdrantVectorStore(
        client=client,
        collection_name=collection,
        embedding=embeddings,
    )
    store.add_documents(all_docs)

    print(f"Qdrant collection: {collection}")

    # Simple per-file stats
    print("\nChunks per file (desc):")
    for src, c in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{c:5d}  {src}")
    total = sum(counts.values())
    avg = total / len(counts) if counts else 0
    print(f"\nFiles: {len(counts)} | Total chunks: {total} | Avg/file: {avg:.2f}")

#frontend\RAG\md_out\www.ncbi.nlm.nih.gov\pmc\articles


if __name__ == "__main__":
    process_markdown_directory(
        in_dir="RAG/md_out/",
        collection="biology_articles_markdown_v2"
    )

