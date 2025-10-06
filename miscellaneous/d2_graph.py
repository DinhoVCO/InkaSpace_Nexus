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
CELLECTION_NAME = "task_proyects"
ARTICLES_COLLECTION_NAME = "abstracts"
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


articles_store = QdrantVectorStore(
        client=client,
        collection_name=ARTICLES_COLLECTION_NAME,
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
# TODO: REPLACE THIS FUNCTION WITH YOUR OWN SEARCH LOGIC
# ==============================================================================
def get_similar_articles(task_query: str, k=10) -> list[str]:
    """
    SIMULATED function that returns a list of similar task IDs.
    """
    st.toast(f"Running similarity search for: '{task_query}'...")

    retrieved_docs = articles_store.similarity_search(task_query, k=5)
    results=[]
    for doc in retrieved_docs:
        print(doc.metadata)
        results.append(doc.metadata['pmcid'])
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
def get_all_articles(path=''):
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

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
        st.session_state.similar_articles = []
    
    with st.form(key='search_form'):
        search_query = st.text_input(
            label="Search by project or research title:",
            placeholder="E.g.: Mice in Bion-M 1 space mission",
             key="search_query"
        )
        col_search, col_clear, _ = st.columns([1, 1.5, 8])
        with col_search:
            submitted = st.form_submit_button("Search")
        with col_clear:
            cleared = st.form_submit_button("Clear Search")

    if submitted and search_query:
        st.session_state.similar_tasks = get_similar_tasks(search_query)
        st.session_state.similar_articles = get_similar_articles(search_query)
        if not st.session_state.similar_tasks:
            st.warning("No similar tasks found for the provided ID.")
            st.session_state.graph_visible = False
        else:
             st.toast(f"Search complete. Showing {len(st.session_state.similar_tasks)} related tasks.")
             st.session_state.graph_visible = True

    if cleared:
        st.session_state.similar_tasks = []
        st.session_state.similar_articles = []
        st.session_state.graph_visible = False
        st.info("Search cleared. Enter a new Task ID to begin.")

        
    path_all_projects = "RAG/all_proyects.json" 
    path_all_articles = "RAG/metadata.json" 
    path_nasa_tasks = "RAG/taskbook/nasa_tasks.json"


    tab1, tab2 = st.tabs(["Knowledge Graph", "Articles"])
    

    with tab1:

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

    with tab2:
        st.markdown("### 🧾 Results")
        data_articles = get_all_articles(path=path_all_articles)
        if not st.session_state.similar_articles:
            st.info("No articles found for this search.")
        else:
            if st.session_state.similar_articles  is None:
                st.session_state.similar_articles = []
            ids_unicos = set(st.session_state.similar_articles)

            # Si quieres volver a lista
            ids_unicos = list(ids_unicos)
            for id_article in ids_unicos:
                art = data_articles[id_article]
                with st.container():
                    st.markdown(f"### {art['title']}")
                    st.markdown(f"**Authors:** {art['authors']}")
                    st.markdown(f"**PMCID:** `{art['pmcid']}` — **Date:** {art['publication_date']}")
                    st.link_button("🔗 View article", f"https://www.ncbi.nlm.nih.gov/pmc/articles/{art['pmcid']}/")

                    #st.link_button("🔗 View article", f"https://www.ncbi.nlm.nih.gov/pmc/articles/{art["pmcid"]}/")
                    # col1, col2 = st.columns([0.2, 0.8])
                    # with col1:
                    #     @st.dialog("Summarize article")
                    #     def show_summarize(title):
                    #         st.subheader(title)
                    #         if st.button("Close"):
                    #             st.session_state.vote = {"item": title}
                    #             st.rerun()
                    #     # Summarize button
                    #     # if st.button("🧠 Summarize", key=f"summ_{art['pmcid']}"):
                    #     #     # st.info(f"Summarizing article *{art['title']}* ... (you can connect to your LLM here)")
                    #     #     show_summarize(art["title"])
                    # with col2:
                    #     # View article button (link to external site)
                    #     st.link_button("🔗 View article", f"https://www.ncbi.nlm.nih.gov/pmc/articles/{art["pmcid"]}/")
                    #     # if st.button("🔗 View", key=f"view_{art['pmcid']}"):
                    #     #     pmcid = art["pmcid"]
                    #     #     st.markdown(f"[Open in PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/)", unsafe_allow_html=True)
                    
                    st.divider()
