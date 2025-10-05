import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_core.messages import HumanMessage, AIMessage


# --- Inicialización del historial de chat en st.session_state ---
# Usamos 'messages' en lugar de 'messages_d1' para mayor claridad
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Interfaz del Chatbot ---
def chatbot_interface(session_messages, graph_to_call, selected_sections=None):
    """Renderiza y gestiona el chatbot conectado a tu LangGraph conversacional."""
    print("Selected Sections:", selected_sections)  # Debugging line
    # Muestra los mensajes previos del historial
    chat_container = st.container(height=450, border=True)

    # Display previous messages
    with chat_container:
        for message in session_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Captura la nueva entrada del usuario
    if prompt := st.chat_input("Escribe tu pregunta sobre biología espacial aquí..."):
        with chat_container:
            # Añade y muestra el mensaje del usuario en la interfaz
            session_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Genera y muestra la respuesta del grafo
            with st.chat_message("assistant"):
                # Usamos un spinner para indicar que el bot está "pensando"
                with st.spinner("Pensando..."):
                    st_callback = StreamlitCallbackHandler(st.container())

                    # --- CAMBIO CLAVE: INVOCACIÓN DEL GRAFO CONVERSACIONAL ---
                    
                    # 1. Formateamos el historial de Streamlit al formato de LangChain
                    formatted_messages = []
                    for msg in session_messages:
                        if msg["role"] == "user":
                            formatted_messages.append(HumanMessage(content=msg["content"]))
                        elif msg["role"] == "assistant":
                            formatted_messages.append(AIMessage(content=msg["content"]))

                    # 2. Invocamos el grafo con el historial completo
                    try:
                        # La entrada ahora es un diccionario con la clave "messages"
                        result = graph_to_call.invoke(
                            {
                                "messages": formatted_messages, 
                                "selected_sections": selected_sections or []
                            },
                            {"callbacks": [st_callback]}
                        )
                        
                        # 3. Extraemos la respuesta del último mensaje del resultado
                        # El grafo devuelve el estado final, donde el último mensaje es la respuesta de la IA
                        response_message = result["messages"][-1]
                        response = response_message

                    except Exception as e:
                        response = f"⚠️ Ocurrió un error al procesar tu solicitud: {e}"
                    # --- FIN DEL CAMBIO CLAVE ---

                    st.markdown(response)
            
            # Añadimos la respuesta del asistente al historial de la sesión
            session_messages.append({"role": "assistant", "content": response})
