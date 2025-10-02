import streamlit as st
import random
import time

def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def chatbot_interface(session_messages):
    """Renderiza un chatbot simple en la interfaz."""   

    # Display chat messages from history on app rerun
    chat_container = st.container(height=400)
    with chat_container:
        for message in session_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with chat_container:
            st.chat_message("user").markdown(prompt)
            # Add user message to chat history
            session_messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                response = st.write_stream(response_generator())
            # Add assistant response to chat history
            session_messages.append({"role": "assistant", "content": response})