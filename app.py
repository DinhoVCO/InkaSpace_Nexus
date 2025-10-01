import streamlit as st
from dashboard_1 import display_dashboard as display_dashboard_1
from dashboard_2 import display_dashboard as display_dashboard_2
from dashboard_3 import display_dashboard as display_dashboard_3


# --- FUNCIÓN PRINCIPAL DE LA APLICACIÓN ---
def main():
    """
    Función principal que gestiona el estado de la selección de usuario.
    """
    # Inicializamos el estado de sesión si no existe
    if 'user_type' not in st.session_state:
        st.session_state.user_type = None

    # Si no hay ningún usuario seleccionado, mostramos la pantalla de selección
    if st.session_state.user_type is None:
        st.set_page_config(page_title="Selección de Usuario", layout="centered")
        st.title("Bienvenido al Sistema de Dashboards")
        
        user_choice = st.selectbox(
            "Por favor, selecciona tu tipo de usuario para continuar:",
            ("Selecciona una opción", "Administrador", "Analista", "Visitante"),
            index=0
        )
        
        # Si el usuario elige una opción válida, la guardamos en el estado y reiniciamos el script
        if user_choice != "Selecciona una opción":
            st.session_state.user_type = user_choice
            st.rerun()
        else:
            st.info("Selecciona un tipo de usuario para ver el dashboard correspondiente.")
    
    # Si ya hay un usuario seleccionado, mostramos el dashboard directamente
    else:
        if st.session_state.user_type == "Administrador":
            display_dashboard_1(st.session_state.user_type)
        elif st.session_state.user_type == "Analista":
            display_dashboard_2(st.session_state.user_type)
        elif st.session_state.user_type == "Visitante":
            display_dashboard_3(st.session_state.user_type)
        else:
            st.error("Tipo de usuario no reconocido. Por favor, reinicia la aplicación.")
            st.session_state.user_type = None
            st.rerun()

if __name__ == "__main__":
    main()

