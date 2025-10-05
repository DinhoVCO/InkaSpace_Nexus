import streamlit as st
from streamlit_agraph import agraph



def get_graph(nodes=[], edges=[], config=None):
    chat_container = st.container(height=400)
    with chat_container:
        return_value = agraph(nodes=nodes, 
                            edges=edges, 
                            config=config)
    return return_value