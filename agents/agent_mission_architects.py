# -----------------------------
# Space Biology QA Pipeline (Mission Architects Profile)
# -----------------------------
import os
import re
from dotenv import load_dotenv
from typing_extensions import List, TypedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TypedDict, Annotated, List

from langchain import hub
from langchain_core.documents import Document
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
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
# Initialize Qdrant clients and embeddings
# -----------------------------
ALL_DOCS_COLLECTION = "biology_articles"
RESULTS_COLLECTION = "task_proyects"
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

embeddings = MistralAIEmbeddings(model="mistral-embed")

# Main collection (scientific papers)
store_all = QdrantVectorStore(
    client=client,
    collection_name=ALL_DOCS_COLLECTION,
    embedding=embeddings
)

# Secondary collection (project results)
store_results = QdrantVectorStore(
    client=client,
    collection_name=RESULTS_COLLECTION,
    embedding=embeddings
)


# -----------------------------
# Load prompts and LLM
# -----------------------------
prompt_mission_architects = hub.pull("pruebanasa/mission_architects")
llm = init_chat_model("open-mixtral-8x7b", model_provider="mistralai")


# -----------------------------
# Define pipeline state schema
# -----------------------------
class State(TypedDict):
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]
    context: List[Document]
    summary: List[str]
    answer: str
    selected_sections: List[str]


# -----------------------------
# Document retrieval step
# -----------------------------
def retrieve_architect(state: dict, k=3) -> dict:
    """
    Retrieves top-k relevant scientific papers and projects related to
    space mission design, safety, and biological/engineering integration.
    Combines both Qdrant collections: all scientific articles and project results.
    """
    question = state["messages"][-1].content
    print(f"[retrieve_architect] Searching for '{question}' across collections...")

    # --- 1. Retrieve from both collections ---
    docs_bio = store_all.similarity_search(query=question, k=k)
    docs_proj = store_results.similarity_search(query=question, k=k)

    retrieved_docs = docs_bio + docs_proj

    if not retrieved_docs:
        print("[retrieve_architect] No relevant mission-related documents found.")
        return {"context": [], "summary": "No mission-related information found."}

    summary_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        meta = doc.metadata or {}

        # Identify if it’s an article or a project
        doc_type = "Scientific Article" if "title" in meta else "Scientific Project"

        # --- Extract common metadata ---
        title = meta.get("title") or meta.get("project_title", "Untitled")
        authors = meta.get("authors", "Unknown")
        publication_date = meta.get("publication_date", meta.get("start_date", "Unknown"))
        pmid = meta.get("pmid", "")
        pub_link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else meta.get("pdf_download_link", "N/A")

        # --- Extract specialized metadata for mission relevance ---
        environment = meta.get("environment", "Not specified (e.g., microgravity, ISS, Mars analog, etc.)")
        mission_relevance = meta.get("mission_relevance", "")
        responsible_center = meta.get("project_information", {}).get("responsible_center", "Unknown")
        division = meta.get("division", "Unknown")
        key_findings = meta.get("key_findings", "") or meta.get("task_progress_and_bibliography", {}).get("task_progress", "")
        earth_benefits = meta.get("project_information", {}).get("research_impact/earth_benefits", "")
        implications = meta.get("implications", "No mission implications specified.")

        # --- Build structured text block ---
        info = f"""Document {i} ({doc_type})
Title: {title}
Authors/PI: {authors}
Date: {publication_date}
Division/Center: {division} / {responsible_center}
Environment: {environment}
Link: {pub_link}

Key Findings / Progress:
{key_findings or 'No findings available.'}

Mission Relevance:
{mission_relevance or implications}

Earth or Habitat Design Impact:
{earth_benefits or 'No direct impact described.'}

Content:
{doc.page_content.strip()}
"""
        summary_blocks.append(info.strip())

    # --- Combine all summaries ---
    summary_text = "\n\n---\n\n".join(summary_blocks)
    print(f"[retrieve_architect] Retrieved {len(retrieved_docs)} relevant documents.")
    return {
        "context": retrieved_docs,
        "summary": summary_text
    }


# -----------------------------
# Answer generation step
# -----------------------------
def generate(state: State) -> State:
    """
    Generates a structured, technical answer to support lunar and Martian mission design,
    integrating biological and experimental research context.
    """
    context = state.get("summary", "")
    chat_history = state["messages"][:-1]

    question = state["messages"][-1].content
    messages = prompt_mission_architects.invoke({
        "question": question,
        "context": context,
        "chat_history": chat_history
    })

    print("[generate] Sending data to LLM (Mission Architect Agent)...")
    response = llm.invoke(messages)
    answer = response.content.strip()

    return {"messages": [answer]}


# -----------------------------
# Pipeline construction
# -----------------------------
graph_builder = StateGraph(State).add_sequence([
    retrieve_architect,   # Retrieve relevant mission-related data
    generate              # Generate analytical and technical response
])

graph_builder.add_edge(START, "retrieve_architect")
graph = graph_builder.compile()
