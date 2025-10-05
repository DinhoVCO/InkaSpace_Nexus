import streamlit as st
from components.chatbot import chatbot_interface
from agents.agent_scientists import graph  # your compiled graph


def render_main_content(user_type):
    """Muestra el contenido de la página principal del dashboard."""
    #st.title(f"{user_type} Dashboard")
    #st.markdown("Este es un esquema interactivo. Las columnas y el chatbot de abajo son placeholders.")
    #st.write("---")

    col1, col2, col3 = st.columns([1.5, 4, 1.5])
    with col3:
        st.markdown("Filter")
        sections = [
            "Abstract",
            "Introduction",
            "Results and Discussion", # Corregido "REselts and Discution"
            "Conclusion",
            "Any Section"
        ]

        for section in sections:
            st.session_state.setdefault(section, True)

        
        with st.expander("Filter by Section", expanded=True):
            for section in sections:
                st.checkbox(section, key=section)

        # Recolectar las secciones que están marcadas
        selected_sections = [s for s in sections if st.session_state[s]]
    with col1:
        st.header("Información Clave")
        st.metric(label="Ventas del Mes", value="1,250", delta="120")
        st.metric(label="Usuarios Activos", value="350", delta="-5%")
    with col2:
        st.header("🤖 ChatBot")
        if "messages_d1" not in st.session_state:
            st.session_state.messages_d1 = []
        chatbot_interface(st.session_state.messages_d1, graph, selected_sections)
                



