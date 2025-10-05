import streamlit as st
# Asumiendo que get_graph está en components/kw_graph.py
# from components.kw_graph import get_graph 
from streamlit_agraph import agraph, Node, Edge, Config
import json
import time

# --- Mock de la función get_graph para que el script se pueda ejecutar ---
def get_graph(nodes, edges, config):
    agraph(nodes=nodes, edges=edges, config=config)
# --------------------------------------------------------------------

# ==============================================================================
# TODO: REEMPLAZA ESTA FUNCIÓN CON TU PROPIA LÓGICA DE BÚSQUEDA
# ==============================================================================
def get_similar_tasks(task_id_query: str) -> list[str]:
    """
    Función SIMULADA que devuelve una lista de IDs de tareas similares.
    """
    st.info(f"Ejecutando búsqueda de similitud para: '{task_id_query}'...")
    time.sleep(1) # Simular latencia de la búsqueda

    mock_data = {
        "80NSSC21K0300": ["80NSSC21K0300", "80NSSC22K0400", "80NSSC20K0500"],
        "NNX16AT22A": ["NNX16AT22A", "NNX15AC31G", "NNX17AB61G"],
        "10062": ["10155", "10174"] 
    }
    
    results = mock_data.get(task_id_query.strip(), [])
    # Si no hay resultados pero el usuario buscó algo, devuelve solo ese ID para visualizarlo
    if not results and task_id_query:
         return [task_id_query.strip()] 
    return results
# ==============================================================================
# FIN DE LA ZONA A REEMPLAZAR
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
    # El resto de esta función no necesita cambios, la lógica de filtrado es correcta.
    # Se deja igual que en la versión anterior.
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
        st.error(f"Error: No se encontró el archivo {e.filename}.")
        return [], [], Config()

    nodes = []
    edges = []
    existing_nodes = set()
    
    task_to_center_map = {
        proj.get('id'): proj.get('project_information', {}).get('responsible_center')
        for proj in all_projects_data
    }

    # Procesar all_projects.json
    for project in all_projects_data:
        task_id = project.get('id')
        if tasks_to_show and task_id not in tasks_to_show:
            continue
        responsible_center = project.get('project_information', {}).get('responsible_center')
        if centers_to_show and responsible_center not in centers_to_show:
            continue
        if 'Task' in node_types_to_show and task_id and task_id not in existing_nodes:
            nodes.append(Node(id=task_id, label=f"Task: {task_id}", shape="dot", color="#FFC75F", size=15))
            existing_nodes.add(task_id)
        if 'Responsible Center' in node_types_to_show and responsible_center and responsible_center not in existing_nodes:
            nodes.append(Node(id=responsible_center, label=responsible_center, shape="square", color="#C34A36", size=20))
            existing_nodes.add(responsible_center)
        if 'Task' in node_types_to_show and 'Responsible Center' in node_types_to_show and task_id and responsible_center:
            edges.append(Edge(source=task_id, target=responsible_center, label="managed_by"))

    # Procesar nasa_tasks.json
    for task in nasa_tasks_data:
        task_id = task.get('Task ID')
        if tasks_to_show and task_id not in tasks_to_show:
            continue
        pubmed_id = task.get('PubMed ID')
        task_center = task_to_center_map.get(task_id)
        if centers_to_show and task_center not in centers_to_show:
            continue
        if pubmed_id and pubmed_id != 'No encontrado':
            if 'PubMed ID' in node_types_to_show and pubmed_id not in existing_nodes:
                nodes.append(Node(id=pubmed_id, label=f"PubMed: {pubmed_id}", shape="triangle", color="#94D2BD", size=10))
                existing_nodes.add(pubmed_id)
            if 'Task' in node_types_to_show and 'PubMed ID' in node_types_to_show and task_id:
                if task_id not in existing_nodes:
                    nodes.append(Node(id=task_id, label=f"Task: {task_id}", shape="dot", color="#FFC75F", size=15))
                    existing_nodes.add(task_id)
                edges.append(Edge(source=task_id, target=pubmed_id, label="has_publication"))
                                
    config = Config(width=900, height=700, directed=True, physics=True, hierarchical=False,
                    nodeHighlightBehavior=True, highlightColor="#F7A7A6")
    return nodes, edges, config

def render_configuration_page():
    st.set_page_config(layout="wide")
    st.title("Knowledge Graph Grants Projects")
    
    if 'graph_visible' not in st.session_state:
        st.session_state.graph_visible = False
        st.session_state.similar_tasks = []

    with st.form(key='search_form'):
        search_query = st.text_input(
            "Buscar Task ID y visualizar tareas similares:",
            placeholder="Ej: 80NSSC21K0300"
        )
        col_search, col_clear, _ = st.columns([1, 1, 8])
        
        with col_search:
            submitted = st.form_submit_button("Buscar")
        with col_clear:
            cleared = st.form_submit_button("Limpiar Búsqueda")

    if submitted and search_query:
        st.session_state.similar_tasks = get_similar_tasks(search_query)
        if not st.session_state.similar_tasks:
            st.warning("No se encontraron tareas similares para el ID proporcionado.")
            st.session_state.graph_visible = False
        else:
             st.success(f"Búsqueda completada. Mostrando {len(st.session_state.similar_tasks)} tareas relacionadas.")
             st.session_state.graph_visible = True

    if cleared:
        st.session_state.similar_tasks = []
        st.session_state.graph_visible = False
        st.info("Búsqueda limpiada. Ingresa un nuevo Task ID para comenzar.")
    
    st.markdown("---")
    
    path_all_projects = "RAG/all_proyects.json" 
    path_nasa_tasks = "RAG/taskbook/nasa_tasks.json"

    col1, col2 = st.columns([1, 4])

    with col1:
        st.header("Filtros del Grafo")
        node_types = ['Task', 'Responsible Center', 'PubMed ID']
        selected_node_types = st.multiselect(
            "Mostrar Tipos de Nodos:", options=node_types, default=node_types
        )
        st.markdown("---")
        
        all_centers = get_all_centers(path_all_projects)
        with st.expander("Filtrar por Centro Responsable", expanded=True):
            selected_centers = []
            # --- CAMBIO CLAVE AQUÍ ---
            # Se establece el valor por defecto en True para que esté marcado al inicio.
            select_all = st.checkbox("Seleccionar/Deseleccionar Todos", value=True)
            for center in all_centers:
                if st.checkbox(center, value=select_all, key=center):
                    selected_centers.append(center)

    with col2:
        st.header("Visualización del Grafo")
        
        if st.session_state.get('graph_visible', False):
            with st.spinner("Generando y dibujando el grafo..."):
                tasks_to_filter = st.session_state.get('similar_tasks', [])
                nodes, edges, config = get_edges_and_nodes(
                    path_all_projects, 
                    path_nasa_tasks,
                    tasks_to_show=tasks_to_filter,
                    node_types_to_show=selected_node_types,
                    centers_to_show=selected_centers
                )
                
                if not nodes:
                    st.warning("No se encontraron nodos con los filtros seleccionados. Por favor, ajusta los filtros en la columna izquierda o limpia la búsqueda.")
                else:
                    get_graph(nodes, edges, config)
                    st.success(f"Grafo generado con {len(nodes)} nodos y {len(edges)} aristas.")
        else:
            st.info("Por favor, realiza una búsqueda de un Task ID para visualizar el grafo de conocimiento.")

