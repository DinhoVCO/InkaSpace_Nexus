import streamlit as st
# Assuming get_graph is in components/kw_graph.py
# from components.kw_graph import get_graph 
from streamlit_agraph import agraph, Node, Edge, Config
import json
from qdrant_client import QdrantClient
from langchain_mistralai import MistralAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
CELLECTION_NAME = "tasks_proyects"
client = QdrantClient(
        url=QDRANT_URL, 
        api_key=QDRANT_API_KEY,
    )
embeddings = MistralAIEmbeddings(model="mistral-embed")
store = QdrantVectorStore(
        client=client,
        collection_name=CELLECTION_NAME,
        embedding=embeddings,
    )



# --- Mock of the get_graph function so the script can be run ---
def get_graph(nodes, edges, config):
    agraph(nodes=nodes, edges=edges, config=config)
# --------------------------------------------------------------------

# ==============================================================================
# TODO: REPLACE THIS FUNCTION WITH YOUR OWN SEARCH LOGIC
# ==============================================================================
def get_similar_tasks(task_query: str, k=10) -> list[str]:
    """
    SIMULATED function that returns a list of similar task IDs.
    """
    st.toast(f"Running similarity search for: '{task_query}'...")

    retrieved_docs = store.similarity_search(task_query, k)
    results=[]
    for doc in retrieved_docs:
        results.append(doc.metadata['id'])
    return results


# ==============================================================================
# END OF THE AREA TO REPLACE
# ==============================================================================


def get_all_centers(path_all_projects='all_projects.json'):
    try:
        with open(path_all_projects, 'r', encoding='utf-8') as f:
            all_projects_data = json.load(f)
        centers = set(
            proj.get('project_information', {}).get('responsible_center')
            for proj in all_projects_data if proj.get('project_information', {}).get('responsible_center')
        )
        return sorted(list(centers))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_edges_and_nodes(
    path_all_projects='all_projects.json', 
    path_nasa_tasks='nasa_tasks.json',
    tasks_to_show=None,
    node_types_to_show=None,
    centers_to_show=None
):
    # The rest of this function does not need changes, the filtering logic is correct.
    # It is left the same as in the previous version.
    if node_types_to_show is None:
        node_types_to_show = ['Task', 'Responsible Center', 'PubMed ID']
    if centers_to_show is None:
        centers_to_show = []

    try:
        with open(path_all_projects, 'r', encoding='utf-8') as f:
            all_projects_data = json.load(f)
        with open(path_nasa_tasks, 'r', encoding='utf-8') as f:
            nasa_tasks_data = json.load(f)
    except FileNotFoundError as e:
        st.error(f"Error: File {e.filename} not found.")
        return [], [], Config()

    nodes = []
    edges = []
    existing_nodes = set()
    
    task_to_center_map = {
        proj.get('id'): proj.get('project_information', {}).get('responsible_center')
        for proj in all_projects_data
    }

    # Process all_projects.json
    for project in all_projects_data:
        
        task_id = project.get('id')
        task_title=f'''Project: {project.get('project_title')}
         Grant Contract:{project.get('project_information').get('grantcontract_no')}
         Division: {project.get('division')}
         '''
        center_title=f'''Responsible center: {project.get('project_information').get('responsible_center')}
         Grant_monitor:{project.get('project_information').get('grant_monitor')}
         '''
        if tasks_to_show and task_id not in tasks_to_show:
            continue
        responsible_center = project.get('project_information', {}).get('responsible_center')
        if centers_to_show and responsible_center not in centers_to_show:
            continue
        if 'Task' in node_types_to_show and task_id and task_id not in existing_nodes:
            nodes.append(Node(id=task_id,title= task_title,label=f"Task: {task_id}", shape="dot", color="#FFC75F", size=15))
            existing_nodes.add(task_id)
        if 'Responsible Center' in node_types_to_show and responsible_center and responsible_center not in existing_nodes:
            nodes.append(Node(id=responsible_center, title=center_title, label=responsible_center, shape="square", color="#C34A36", size=20))
            existing_nodes.add(responsible_center)
        if 'Task' in node_types_to_show and 'Responsible Center' in node_types_to_show and task_id and responsible_center:
            edges.append(Edge(source=task_id, target=responsible_center, label="managed_by"))

    # Process nasa_tasks.json
    for task in nasa_tasks_data:

        task_id = task.get('Task ID')
        task_title=f'''Project: {task.get('Project Name')}'''
        pubmed_title=f'''Article Title: {task.get('Article Title')}
         DOI:{task.get('DOI')}
         PubMed ID: {task.get('PubMed ID')}
         '''
        if tasks_to_show and task_id not in tasks_to_show:
            continue
        pubmed_id = task.get('PubMed ID')
        task_center = task_to_center_map.get(task_id)
        if centers_to_show and task_center not in centers_to_show:
            continue
        if pubmed_id and pubmed_id != 'No encontrado':
            if 'PubMed ID' in node_types_to_show and pubmed_id not in existing_nodes:
                nodes.append(Node(id=pubmed_id, title=pubmed_title, label=f"PubMed: {pubmed_id}", shape="triangle", color="#94D2BD", size=10))
                existing_nodes.add(pubmed_id)
            if 'Task' in node_types_to_show and 'PubMed ID' in node_types_to_show and task_id:
                if task_id not in existing_nodes:
                    nodes.append(Node(id=task_id, title=task_title, label=f"Task: {task_id}", shape="dot", color="#FFC75F", size=15))
                    existing_nodes.add(task_id)
                edges.append(Edge(source=task_id, target=pubmed_id, label="has_publication"))
                                        
    config = Config(width=1200, height=400, directed=True, physics=True, hierarchical=False,
                    nodeHighlightBehavior=True, highlightColor="#F7A7A6")
    return nodes, edges, config

def render_graph_page():

    st.set_page_config(layout="wide")
    st.title("Knowledge Graph")
    
    if 'graph_visible' not in st.session_state:
        st.session_state.graph_visible = False
        st.session_state.similar_tasks = []

    with st.form(key='search_form'):
        col_query, col_number = st.columns([8, 2])
        with col_query:
            search_query = st.text_input(
                label="Search by project or research title:",
                placeholder="E.g.: Mice in Bion-M 1 space mission"
            )
        with col_number:
            top_k = st.number_input("Number of similar tasks to retrieve:", min_value=1, max_value=15, value=7, step=1)
        col_search, col_clear, _ = st.columns([1, 1.5, 8])
        with col_search:
            submitted = st.form_submit_button("Search")
        with col_clear:
            cleared = st.form_submit_button("Clear Search")

    if submitted and search_query:
        st.session_state.similar_tasks = get_similar_tasks(search_query, top_k)
        if not st.session_state.similar_tasks:
            st.warning("No similar tasks found for the provided ID.")
            st.session_state.graph_visible = False
        else:
             st.toast(f"Search complete. Showing {len(st.session_state.similar_tasks)} related tasks.")
             st.session_state.graph_visible = True

    if cleared:
        st.session_state.similar_tasks = []
        st.session_state.graph_visible = False
        st.info("Search cleared. Enter a new Task ID to begin.")
        
    path_all_projects = "RAG/all_proyects.json" 
    path_nasa_tasks = "RAG/taskbook/nasa_tasks.json"

    col1, col2 = st.columns([1, 4])
    
    with col1:
        container_1 = st.container(border=True)
        with container_1:
            st.markdown("### Graph Filters")
            node_types = ['Task', 'Responsible Center', 'PubMed ID']
            selected_node_types = st.multiselect(
                "Show Node Types:", options=node_types, default=node_types
            )
            
            all_centers = get_all_centers(path_all_projects)
            with st.expander("Filter by Responsible Center", expanded=True):
                selected_centers = []
                # --- KEY CHANGE HERE ---
                # The default value is set to True so it is checked initially.
                for center in all_centers:
                    if st.checkbox(center, value=True, key=center):
                        selected_centers.append(center)

    with col2:
        st.markdown("### Graph Visualization")
        container_2 = st.container(border=True)
        with container_2:
            if st.session_state.get('graph_visible', False):
                with st.spinner("Generating and drawing the graph..."):
                    tasks_to_filter = st.session_state.get('similar_tasks', [])
                    nodes, edges, config = get_edges_and_nodes(
                        path_all_projects, 
                        path_nasa_tasks,
                        tasks_to_show=tasks_to_filter,
                        node_types_to_show=selected_node_types,
                        centers_to_show=selected_centers
                    )
                    
                    if not nodes:
                        st.warning("No nodes found with the selected filters. Please adjust the filters in the left column or clear the search.")
                    else:
                        get_graph(nodes, edges, config)
                        st.success(f"Graph generated with {len(nodes)} nodes and {len(edges)} edges.")
            else:
                st.info("Please perform a search for a Task ID to visualize the knowledge graph.")

