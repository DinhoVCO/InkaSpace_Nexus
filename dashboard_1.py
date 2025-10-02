# dashboard_1.py (modificado para manejar vistas internas)
import streamlit as st
import pandas as pd
import numpy as np

# --- Define aquí las funciones que renderizan cada "página" ---

def render_main_content(user_type):
    """Muestra el contenido de la página principal del dashboard."""
    st.title(f"Bienvenido al Dashboard, {user_type}")
    st.markdown("Este es un esquema interactivo. Las columnas y el chatbot de abajo son placeholders.")
    st.write("---")

    col1, col2, col3 = st.columns([1.5, 4, 1.5])
    with col1:
        st.header("Información Clave")
        st.metric(label="Ventas del Mes", value="1,250", delta="120")
        st.metric(label="Usuarios Activos", value="350", delta="-5%")
    with col2:
        st.header("🤖 Asistente Virtual")
        st.info("El chatbot iría aquí.")
    with col3:
        st.header("Herramientas")
        st.button("Exportar Datos a CSV", use_container_width=True)

def render_analisis_page():
    """Muestra el contenido de la página de Análisis de Datos."""
    st.title("📊 Análisis de Datos")
    st.markdown("Esta página muestra gráficos y tablas interactivas.")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Ventas', 'Costos', 'Beneficios'])
    st.line_chart(chart_data)
    st.dataframe(chart_data)

def render_configuracion_page():
    """Muestra el contenido de la página de Configuración."""
    st.title("⚙️ Configuración de la Cuenta")
    st.markdown("Aquí puedes ajustar las preferencias de tu cuenta.")
    st.text_input("Correo Electrónico", value="admin@email.com")
    st.selectbox("Idioma", ["Español", "Inglés"])
    st.button("Guardar Cambios", type="primary")


# --- FUNCIÓN PRINCIPAL DEL DASHBOARD ---

def display_dashboard(user_type):
    """
    Muestra el dashboard y gestiona la navegación interna basada en st.session_state.view
    """
    st.set_page_config(page_title=f"Dashboard para {user_type}", layout="wide")

    # --- 1. SIDEBAR (SIEMPRE VISIBLE) ---
    with st.sidebar:
        st.title(f"Panel de {user_type}")
        st.write("---")
        st.write("Navegación Principal")

        # --- BOTONES DE NAVEGACIÓN ---
        # Cada botón cambia el estado 'view' y fuerza un rerun
        if st.button("Página Principal", use_container_width=True):
            st.session_state.view = 'principal'
            st.rerun()
        
        if st.button("Análisis de Datos", use_container_width=True):
            st.session_state.view = 'analisis'
            st.rerun()
            
        if st.button("Configuración", use_container_width=True):
            st.session_state.view = 'configuracion'
            st.rerun()

        st.write("---")

        # Botón para cambiar de usuario (reinicia el estado)
        if st.button("Cambiar de Usuario", use_container_width=True, type="primary"):
            st.session_state.user_type = None
            st.session_state.view = 'principal' # Resetea la vista
            st.rerun()

    # --- 2. RENDERIZADO DEL CONTENIDO PRINCIPAL ---
    # Usamos el valor de st.session_state.view para decidir qué función llamar
    
    if st.session_state.view == 'principal':
        render_main_content(user_type)
    elif st.session_state.view == 'analisis':
        render_analisis_page()
    elif st.session_state.view == 'configuracion':
        render_configuracion_page()
    else:
        # Fallback por si el estado se corrompe
        st.warning("Vista no reconocida. Volviendo a la página principal.")
        st.session_state.view = 'principal'
        st.rerun()