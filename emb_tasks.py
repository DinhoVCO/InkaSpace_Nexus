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
import json
load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
                              # Number of results
    

def process_markdown_directory(json_file_path: str, collection: str):
    """Main function to process markdown files and store them into a local Qdrant vector database."""
    

    # 1) Collect & split
    all_docs = []
    counts = defaultdict(int)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        projects = json.load(f)
        for i, project in enumerate(projects):
            text = project['project_information']['task_description']
            doc = Document(page_content=text, metadata=project)       
            all_docs.append(doc)
    print(f"Collected {len(all_docs)}.")
    # 2) Embeddings
    embeddings = MistralAIEmbeddings(model="mistral-embed")
    # 3) Local embedded Qdrant (persists under qdrant_dir)
    client = QdrantClient(
        url=QDRANT_URL, 
        api_key=QDRANT_API_KEY,
    )
    print(all_docs[0])

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
        json_file_path="RAG/all_proyects.json",
        collection="tasks_proyects"
    )
