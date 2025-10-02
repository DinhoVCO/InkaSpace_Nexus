import streamlit as st
from components.chatbot import chatbot_interface

def render_main_content(user_type):
    """Muestra el contenido de la página principal del dashboard."""
    #st.title(f"{user_type} Dashboard")
    #st.markdown("Este es un esquema interactivo. Las columnas y el chatbot de abajo son placeholders.")
    #st.write("---")

    col1, col2, col3 = st.columns([1.5, 4, 1.5])
    with col1:
        st.header("Información Clave")
        st.markdown("Aquí puedes mostrar métricas importantes, KPIs o accesos directos.")
        st.metric(label="Ventas del Mes", value="1,250", delta="120")
        st.metric(label="Usuarios Activos", value="350", delta="-5%")
        with st.expander("Ver más detalles"):
            st.write("Detalles adicionales sobre las métricas mostradas.")

    with col2:
        st.header("🤖 ChatBot")
        if "messages_d3" not in st.session_state:
            st.session_state.messages_d3 = []
        chatbot_interface(st.session_state.messages_d3)
                
    with col3:
        st.header("Herramientas")
        st.markdown("Widgets, filtros o acciones rápidas.")
        st.checkbox("Activar modo oscuro")
        st.selectbox("Seleccionar Periodo", ["Últimos 7 días", "Último mes", "Último trimestre"])
        st.button("Exportar Datos a CSV", use_container_width=True)
        st.write("---")
        st.warning("Notificaciones o alertas importantes pueden ir en esta sección.")
