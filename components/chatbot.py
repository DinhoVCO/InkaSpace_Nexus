import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from agents.agent import graph  # your compiled graph

# --- Initial configuration ---
st.set_page_config(page_title="LangGraph Chatbot", layout="centered")

# Initialize default conversation history
if "messages_d1" not in st.session_state:
    st.session_state.messages_d1 = []

# --- Chatbot interface ---
def chatbot_interface(session_messages):
    """Renders a chatbot connected to your LangGraph"""
    chat_container = st.container()

    # Display previous messages
    with chat_container:
        for message in session_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Type your message..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        session_messages.append({"role": "user", "content": prompt})

        # Graph (LangGraph) response
        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container())
            try:
                result = graph.invoke({"question": prompt}, {"callbacks": [st_callback]})
                response = result.get("answer", "No response.")
            except Exception as e:
                response = f"⚠️ Error running the graph: {e}"

            st.markdown(response)
            session_messages.append({"role": "assistant", "content": response})

# Run the chatbot with the specific dashboard history
chatbot_interface(st.session_state.messages_d1)
