# -----------------------------
# Space Biology QA Pipeline (Manager Profile)
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
# Initialize Qdrant client and embeddings
# -----------------------------
collection_name = "task_proyects"
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

embeddings = MistralAIEmbeddings(model="mistral-embed")

store = QdrantVectorStore(
    client=client,
    collection_name=collection_name,
    embedding=embeddings
)


# -----------------------------
# Load prompts and LLM
# -----------------------------
prompt_manager_latest = hub.pull("pruebanasa/manager_latest")
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
def retrieve_manager(state: dict, k=5) -> dict:
    """
    Retrieves the top-k most relevant NASA project documents (Manager profile)
    from Qdrant and builds a concise summary including project scope,
    funding information, progress, and Earth/space impact.
    """
    question = state["messages"][-1].content
    retrieved_docs = store.similarity_search(query=question, k=k)

    if not retrieved_docs:
        print("[retrieve_manager] No relevant projects found.")
        return {"context": [], "summary": "No relevant projects found."}

    summary_blocks = []
    for i, doc in enumerate(retrieved_docs, start=1):
        meta = doc.metadata or {}

        # --- Safe extraction of metadata fields ---
        project_title = meta.get("project_title", "Untitled")
        fiscal_year = meta.get("fiscal_year", "Unknown")
        division = meta.get("division", "Unknown")
        responsible_center = meta.get("project_information", {}).get("responsible_center", "Unknown")
        principal_investigator = meta.get("principal_investigator", {}).get("name", "Not specified")
        grant_monitor = meta.get("project_information", {}).get("grant_monitor", "Unknown")
        start_date = meta.get("start_date", "Unknown")
        end_date = meta.get("end_date", "Unknown")
        funding_source = meta.get("project_information", {}).get("solicitation__funding_source", "Unknown")
        grant_no = meta.get("project_information", {}).get("grantcontract_no", "Unknown")
        link = meta.get("pdf_download_link", "N/A")

        task_description = (
            meta.get("project_information", {}).get("task_description", "")
            or "No project description available."
        )
        task_progress = (
            meta.get("task_progress_and_bibliography", {}).get("task_progress", "")
            or "No progress report available."
        )
        earth_benefits = (
            meta.get("project_information", {}).get("research_impact/earth_benefits", "")
            or "No Earth benefits described."
        )

        # --- Build formatted text block for each document ---
        info = f"""Project {i}
Title: {project_title}
Division: {division}
Fiscal Year: {fiscal_year}
Responsible Center: {responsible_center}
Principal Investigator: {principal_investigator}
Grant Monitor: {grant_monitor}
Start Date: {start_date}
End Date: {end_date}
Funding Source: {funding_source}
Grant/Contract No.: {grant_no}
Link: {link}

Description:
{task_description}

Progress Summary:
{task_progress}

Impact and Earth Benefits:
{earth_benefits}
"""
        summary_blocks.append(info.strip())

    summary_text = "\n\n---\n\n".join(summary_blocks)
    print(f"[retrieve_manager] Retrieved {len(retrieved_docs)} relevant projects.")
    return {
        "context": retrieved_docs,
        "summary": summary_text
    }


# -----------------------------
# Answer generation step
# -----------------------------
def generate(state: State) -> State:
    """
    Generates the final answer based on the retrieved project context.
    """
    context = state.get("summary", [])
    chat_history = state["messages"][:-1]

    question = state["messages"][-1].content
    messages = prompt_manager_latest.invoke({
        "question": question,
        "context": context,
        "chat_history": chat_history
    })

    response = llm.invoke(messages)
    answer = response.content.strip()

    return {"messages": [answer]}


# -----------------------------
# Pipeline construction
# -----------------------------
graph_builder = StateGraph(State).add_sequence([
    retrieve_manager,   # Retrieve relevant project documents
    generate            # Generate the final synthesized answer
])

graph_builder.add_edge(START, "retrieve_manager")
graph = graph_builder.compile()
