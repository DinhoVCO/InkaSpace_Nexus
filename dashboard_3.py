import streamlit as st

def display_dashboard(user_type):
    """
    Muestra el dashboard principal basado en el tipo de usuario.
    También incluye un botón para cambiar de usuario.
    """
    # --- 1. CONFIGURACIÓN DE LA PÁGINA ---
    # st.set_page_config se puede llamar aquí porque esta función
    # ahora controla toda la vista principal después de la selección.
    st.set_page_config(page_title=f"Dashboard para {user_type}", layout="wide")

    # --- 2. SIDEBAR (BARRA LATERAL) ---
    with st.sidebar:
        st.title(f"Panel de {user_type}")
        st.write("---")
        st.write("Navegación Principal")
        st.button("Página Principal", use_container_width=True)
        st.button("Análisis de Datos", use_container_width=True)
        st.button("Configuración", use_container_width=True)
        st.write("---")

        # Botón para cambiar de usuario (reinicia el estado)
        if st.button("Cambiar de Usuario", use_container_width=True, type="primary"):
            st.session_state.user_type = None
            st.rerun() # Forzamos el reinicio del script para mostrar la selección

        st.info("Esta es una barra lateral donde puedes agregar filtros, enlaces de navegación o información adicional.")

    # --- 3. TÍTULO PRINCIPAL DEL DASHBOARD ---
    st.title(f"Bienvenido al Dashboard, {user_type}")
    st.markdown("Este es un esquema interactivo. Las columnas y el chatbot de abajo son placeholders.")
    st.write("---")

    # --- 4. CREACIÓN DE LAS 3 COLUMNAS ---
    col1, col2, col3 = st.columns([1.5, 4, 1.5])

    # --- Columna Izquierda ---
    with col1:
        st.header("Información Clave")
        st.markdown("Aquí puedes mostrar métricas importantes, KPIs o accesos directos.")
        st.metric(label="Ventas del Mes", value="1,250", delta="120")
        st.metric(label="Usuarios Activos", value="350", delta="-5%")
        with st.expander("Ver más detalles"):
            st.write("Detalles adicionales sobre las métricas mostradas.")

    # --- Columna Central (Chatbot) ---
    with col2:
        st.header("🤖 Asistente Virtual")
        st.markdown("Interactúa con nuestro chatbot para obtener ayuda.")
        chat_container = st.container(height=400)
        with chat_container:
            st.chat_message("assistant").write(f"¡Hola {user_type}! ¿En qué puedo ayudarte hoy?")
            st.chat_message("user").write("Me gustaría ver el reporte de ventas del último trimestre.")
            st.chat_message("assistant").write("Claro, generando el reporte de ventas. Lo encontrarás en la sección de 'Análisis de Datos'.")
        prompt = st.chat_input("Escribe tu mensaje aquí...")
        if prompt:
            with chat_container:
                st.chat_message("user").write(prompt)
                st.chat_message("assistant").write(f"Procesando tu solicitud: '{prompt}'...")

    # --- Columna Derecha ---
    with col3:
        st.header("Herramientas")
        st.markdown("Widgets, filtros o acciones rápidas.")
        st.checkbox("Activar modo oscuro")
        st.selectbox("Seleccionar Periodo", ["Últimos 7 días", "Último mes", "Último trimestre"])
        st.button("Exportar Datos a CSV", use_container_width=True)
        st.write("---")
        st.warning("Notificaciones o alertas importantes pueden ir en esta sección.")
