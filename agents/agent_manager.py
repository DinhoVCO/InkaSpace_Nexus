import os
from dotenv import load_dotenv

# --- LangChain & LangGraph Imports ---
from langchain import hub
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_mistralai import MistralAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.chat_models import init_chat_model # Asumo que esta es una función tuya

from langgraph.graph import StateGraph, START
from typing import TypedDict, Annotated, List

from qdrant_client import QdrantClient

# --- Carga de Variables de Entorno ---
load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
collection_name = "biology_articles_v3"

# ==============================================================================
# 1. CONFIGURACIÓN DEL RETRIEVER Y EL LLM (Sin cambios)
# ==============================================================================

# Conexión al cliente de Qdrant
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Modelo de embeddings
embeddings = MistralAIEmbeddings(model="mistral-embed")

# Vector store para actuar como retriever
store = QdrantVectorStore(
    client=client,
    collection_name=collection_name,
    embedding=embeddings,
)
retriever = store.as_retriever()

# Modelo de lenguaje
llm = init_chat_model("open-mixtral-8x7b", model_provider="mistralai")

# ==============================================================================
# 2. NUEVO ESTADO CONVERSACIONAL
#    Este es el cambio más importante. En lugar de una 'question',
#    gestionamos una lista de 'messages'.
# ==============================================================================

class State(TypedDict):
    """
    El estado del grafo.
    
    Atributos:
        messages: La lista de mensajes que forman la conversación. 
                  'add_messages' asegura que los nuevos mensajes se añadan a la lista.
        context: La lista de documentos recuperados para la pregunta actual.
    """
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]
    context: List[Document]

# ==============================================================================
# 3. PROMPT CONVERSACIONAL CON CONTEXTO (RAG)
#    Este prompt está diseñado para chat. Entiende el historial,
#    el contexto y la pregunta actual por separado.
# ==============================================================================

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, just say that you don't know. "
    "Keep the answer concise and helpful."
    "\n\n"
    "Context:\n{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

# ==============================================================================
# 4. NODOS DEL GRAFO ADAPTADOS PARA CONVERSACIÓN
# ==============================================================================

def retrieve_documents(state: State) -> dict:
    """
    Recupera documentos basados en la última pregunta del usuario.
    """
    # La pregunta actual es el último mensaje en la lista
    question = state["messages"][-1].content
    
    retrieved_docs = retriever.invoke(question)
    
    
    return {"context": retrieved_docs}

def generate_answer(state: State) -> dict:
    """
    Genera una respuesta usando el LLM, considerando el historial y el contexto.
    """
    
    # Obtenemos los datos del estado
    question = state["messages"][-1].content
    context = state["context"]
    chat_history = state["messages"][:-1] # El historial sin la última pregunta

    # Creamos la cadena de RAG
    rag_chain = prompt | llm

    # Invocamos la cadena con toda la información necesaria
    response = rag_chain.invoke({
        "question": question,
        "context": context,
        "chat_history": chat_history
    })
    
    # Devolvemos la respuesta del LLM para que se añada al historial de mensajes
    return {"messages": [response]}

# ==============================================================================
# 5. CONSTRUCCIÓN Y COMPILACIÓN DEL GRAFO CONVERSACIONAL
# ==============================================================================

graph_builder = StateGraph(State)

# Se añaden los nodos al grafo
graph_builder.add_node("retrieve_documents", retrieve_documents)
graph_builder.add_node("generate_answer", generate_answer)

# Se definen las aristas (el flujo de trabajo)
graph_builder.add_edge(START, "retrieve_documents")
graph_builder.add_edge("retrieve_documents", "generate_answer")

# Se compila el grafo en un objeto ejecutable
graph = graph_builder.compile()
