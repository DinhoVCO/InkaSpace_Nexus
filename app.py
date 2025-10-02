# app.py (modified)
import streamlit as st

# Asumimos que tienes estos archivos, si no, deberías crearlos
# For demonstration purposes, we'll create placeholder functions if files don't exist.

from dashboards.dashboard_1 import display_dashboard as display_dashboard_1
from dashboards.dashboard_2 import display_dashboard as display_dashboard_2
from dashboards.dashboard_3 import display_dashboard as display_dashboard_3




# --- MAIN APPLICATION FUNCTION ---
def main():
    """
    Main function that manages the user selection state.
    """
    # Initialize session states if they don't exist
    if 'user_type' not in st.session_state:
        st.session_state.user_type = None
    if 'view' not in st.session_state:
        st.session_state.view = 'main'  # Default view

    # If no user is selected, show the selection screen
    if st.session_state.user_type is None:
        st.set_page_config(page_title="User Selection", layout="centered")
        col1, col2, col3 = st.columns([1.5, 1, 1.5]) # Adjust the ratio for desired spacing

        with col2:
            st.image("images/logo_nexus.png", use_container_width=True)
        #st.image("images/logo_nexus.png", width=150)
        #st.title("NASA Nexus 🚀")
        st.markdown("<h1 style='text-align: center;'>NASA Nexus 🚀</h1>", unsafe_allow_html=True)


        # Define the new user types based on the target audience
        user_options = [
            "Select an option",
            "Scientist 🔬",
            "Manager 💼",
            "Mission architect 👷🏻‍♂️"
        ]

        user_choice = st.selectbox(
            "Please, select your user type to continue:",
            options=user_options,
            index=0
        )

        # If the user chooses a valid option, save it and set the main view
        if user_choice != "Select an option":
            st.session_state.user_type = user_choice
            st.session_state.view = 'main'  # <-- KEY CHANGE! Reset the view to 'main'
            st.rerun()
        else:
            st.info("""
                    Select a user type to see the corresponding dashboard\n\n
                     - **Scientists** 🔬 who are generating new hypotheses\n
                     - **Managers** 💼 identifying opportunities for investment\n
                     - **Mission architects** 👷🏻‍♂️ looking to explore the Moon and Mars safely and efficiently
            """, icon="ℹ️")

    # If a user is already selected, show the corresponding dashboard
    else:
        # Match the selected user type to its corresponding dashboard function
        if st.session_state.user_type == "Scientist 🔬":
            display_dashboard_1(st.session_state.user_type)
        elif st.session_state.user_type == "Manager 💼":
            display_dashboard_2(st.session_state.user_type)
        elif st.session_state.user_type == "Mission architect 👷🏻‍♂️":
            display_dashboard_3(st.session_state.user_type)
        else:
            st.error("User type not recognized. Please restart the application.")
            st.session_state.user_type = None
            st.rerun()


if __name__ == "__main__":
    main()