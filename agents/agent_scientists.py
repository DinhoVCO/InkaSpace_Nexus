# -----------------------------
# Space Biology QA Pipeline
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
# Initialize Qdrant and embeddings
# -----------------------------
COLLECTION_MAP = {
    "Abstract": "abstracts",
    "Introduction": "introductions",
    "Results and Discussion": "results_discussion",
    "Conclusion": "conclusions",
    "Any Section": "biology_articles"
}
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

embeddings = MistralAIEmbeddings(model="mistral-embed")


# -----------------------------
# Load LLM and research prompt
# -----------------------------
hub_simple = hub.pull("pruebanasa/researcher_simple")
hub_strict = hub.pull("pruebanasa/research_old")
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
    prompt_type: str

def retrieve(state: dict, k=3) -> dict:
    """
    Retrieves documents depending on user-selected sections.
    """
    selected_sections = state.get("selected_sections", ["Any Section"])
    print(f"[retrieve] Selected filters: {selected_sections}")

    # If "Any Section" is chosen, search in the general collection
    if "Any Section" in selected_sections:
        collections_to_search = ["biology_articles"]
    else:
        # Map selected sections to their corresponding collections
        collections_to_search = [
            COLLECTION_MAP[s] for s in selected_sections if s in COLLECTION_MAP
        ]

    question = state["messages"][-1].content
    retrieved_docs = []
    for collection in collections_to_search:
        print(f"[retrieve] Searching in collection: {collection}")

        store = QdrantVectorStore(
            client=client,
            collection_name=collection,
            embedding=embeddings
        )

        # Add top results for this section
        results = store.similarity_search(query=question, k=k)
        retrieved_docs.extend(results)

    if not retrieved_docs:
        print("[retrieve] No similar documents were found.")
        return {"context": [], "summary": "No results found."}

    # Format results
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
    print(f"[retrieve] Retrieved {len(retrieved_docs)} documents in total.")
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
    chat_history = state["messages"][:-1]
    if state["prompt_type"] == "Simple":
        hub = hub_simple
    else:
        hub = hub_strict

    print("*************usando**********")
    print(state["prompt_type"])

    question = state["messages"][-1].content
    messages = hub.invoke({
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
    retrieve,   # Retrieve relevant documents
    generate    # Generate the final answer
])

graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()