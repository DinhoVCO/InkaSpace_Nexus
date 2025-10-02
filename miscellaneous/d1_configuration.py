import streamlit as st

def render_configuration_page():
    """Muestra el contenido de la página de Configuración."""
    st.title("⚙️ Configuración de la Cuenta")
    st.markdown("Aquí puedes ajustar las preferencias de tu cuenta.")
    st.text_input("Correo Electrónico", value="admin@email.com")
    st.selectbox("Idioma", ["Español", "Inglés"])
    st.button("Guardar Cambios", type="primary")