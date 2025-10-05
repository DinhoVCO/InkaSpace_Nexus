
import bs4
from langchain import hub
# from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from langchain.chat_models import init_chat_model
import sys
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from langchain_mistralai import MistralAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os

load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")



# qdrant_dir = sys.argv[1]
collection_name = "biology_articles"


# Open local (embedded) Qdrant DB folder
client = QdrantClient(
        url=QDRANT_URL, 
        api_key=QDRANT_API_KEY,
    )

# Same embedding model used when building the collection
embeddings = MistralAIEmbeddings(model="mistral-embed")

# Create a LangChain vector store bound to the existing collection
store = QdrantVectorStore(
    client=client,
    collection_name=collection_name,
    embedding=embeddings,
)



prompt = hub.pull("rlm/rag-prompt")

llm = init_chat_model("open-mixtral-8x7b", model_provider="mistralai")

# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


# Define application steps
def retrieve(state: State):
    retrieved_docs = store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    #=================================
    assert len(messages.to_messages()) == 1
    #=================================
    return {"answer": response.content}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()
