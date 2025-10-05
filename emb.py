from pathlib import Path
from collections import defaultdict
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
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
    

def process_markdown_directory(in_dir: str, collection: str):
    """Main function to process markdown files and store them into a local Qdrant vector database."""
    
    in_dir = Path(in_dir)

    # 1) Collect & split
    all_docs = []
    counts = defaultdict(int)
    for md_path in in_dir.rglob("*.md"):
        text = md_path.read_text(encoding="utf-8", errors="ignore")
        docs = split_markdown(text)
        for d in docs:
            d.metadata = {"source": md_path.as_posix(), **(d.metadata or {})}
        all_docs.extend(docs)
        counts[md_path.as_posix()] += len(docs)

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

    #print(f"Qdrant collection: {collection}")

    # Simple per-file stats
    #print("\nChunks per file (desc):")
    #for src, c in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    #    print(f"{c:5d}  {src}")
    total = sum(counts.values())
    avg = total / len(counts) if counts else 0
    print(f"\nFiles: {len(counts)} | Total chunks: {total} | Avg/file: {avg:.2f}")

#frontend\RAG\md_out\www.ncbi.nlm.nih.gov\pmc\articles


if __name__ == "__main__":
    process_markdown_directory(
        in_dir="RAG/md_out/",
        collection="biology_articles_v3"
    )
