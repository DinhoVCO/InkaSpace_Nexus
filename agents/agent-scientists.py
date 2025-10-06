# -----------------------------
# Space Biology QA Pipeline
# -----------------------------
import os
import re
from dotenv import load_dotenv
from typing_extensions import List, TypedDict
from concurrent.futures import ThreadPoolExecutor, as_completed

from langchain import hub
from langchain_core.documents import Document
from langchain.chat_models import init_chat_model
from qdrant_client import QdrantClient
from langchain_mistralai import MistralAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langgraph.graph import START, StateGraph

# -----------------------------
# Environment setup
# -----------------------------
load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")


# -----------------------------
# Initialize Qdrant and embeddings
# -----------------------------
collection_name = "biology_articles"
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

embeddings = MistralAIEmbeddings(model="mistral-embed")

store = QdrantVectorStore(
    client=client,
    collection_name=collection_name,
    embedding=embeddings
)


# -----------------------------
# Load LLM and research prompt
# -----------------------------
prompt_research_old = hub.pull("pruebanasa/research_old")
llm = init_chat_model("open-mixtral-8x7b", model_provider="mistralai")


# -----------------------------
# Define pipeline state schema
# -----------------------------
class State(TypedDict):
    question: str
    context: List[Document]
    summary: List[str]
    answer: str


# -----------------------------
# Document retrieval step
# -----------------------------
def retrieve(state: dict, k=15) -> dict:
    """
    Retrieves the top-k most similar documents from Qdrant
    and generates a structured summary containing title, date,
    authors, link, and content (chunk) of each document.
    """
    retrieved_docs = store.similarity_search(query=state["question"], k=k)

    if not retrieved_docs:
        print("[retrieve] No similar documents were found.")
        return {"context": [], "summary": "No results found."}

    summary_list = []
    for i, doc in enumerate(retrieved_docs, start=1):
        meta = doc.metadata
        pmid = meta.get("pmid", "")
        pub_link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "N/A"

        info = f"""Document {i}
Title: {meta.get('title', 'Untitled')}
Publication date: {meta.get('publication_date', 'Unknown')}
Authors: {meta.get('authors', 'Unknown')}
Link: {pub_link}
Content:
{doc.page_content.strip()}
"""
        summary_list.append(info)

    summary_text = "\n".join(summary_list)
    print(f"[retrieve] Retrieved {len(retrieved_docs)} documents")
    return {
        "context": retrieved_docs,
        "summary": summary_text
    }


# -----------------------------
# Answer generation step
# -----------------------------
def generate(state: State) -> State:
    """
    Generates the final answer based on the retrieved context.
    """
    context = state.get("summary", [])

    messages = prompt_research_old.invoke({
        "question": state["question"],
        "context": context
    })

    response = llm.invoke(messages)
    answer = response.content.strip()

    state.update({
        "answer": answer,
    })
    return state


# -----------------------------
# Pipeline construction
# -----------------------------
graph_builder = StateGraph(State).add_sequence([
    retrieve,   # Retrieve relevant documents
    generate    # Generate the final answer
])

graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()