# dashboard_1.py (modified to handle internal views)
import streamlit as st
from miscellaneous.d2_main import render_main_content
from miscellaneous.d2_graph import render_graph_page


def display_dashboard(user_type):
    """
    Displays the dashboard and manages internal navigation based on st.session_state.view
    """
    st.set_page_config(page_title=f"Dashboard for {user_type}", layout="wide")
    st.logo("images/logo_nexus.png", size='large')

    # --- 1. SIDEBAR (ALWAYS VISIBLE) ---
    with st.sidebar:
        st.title(f"{user_type} Panel")
        st.write("---")
        st.write("Main Navigation")

        # --- NAVIGATION BUTTONS ---
        # Each button changes the 'view' state and forces a rerun
        if st.button("AI Search Agent", use_container_width=True):
            st.session_state.view = 'main'
            st.rerun()
        
        if st.button("Research Graph", use_container_width=True):
            st.session_state.view = 'graph'
            st.rerun()

        st.write("---")

        # Button to change user (resets the state)
        if st.button("Change User", use_container_width=True, type="primary"):
            st.session_state.user_type = None
            st.session_state.view = 'main' # Resets the view
            st.rerun()

    # --- 2. RENDER MAIN CONTENT ---
    # We use the value of st.session_state.view to decide which function to call
    
    if st.session_state.view == 'main':
        render_main_content(user_type)
    elif st.session_state.view == 'graph':
        render_graph_page()
    else:
        # Fallback in case the state gets corrupted
        st.warning("Unrecognized view. Returning to the main page.")
        st.session_state.view = 'main'
        st.rerun()