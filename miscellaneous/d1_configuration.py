import streamlit as st
from components.kw_graph import get_graph
from streamlit_agraph import agraph, Node, Edge, Config
import json

def get_edges_and_nodes(path_all_projects='all_projects.json', path_nasa_tasks='nasa_tasks.json'):
    """
    Carga datos de 'all_projects.json' y 'nasa_tasks.json' para crear nodos y aristas
    para una visualización de grafos.
    """
    try:
        # Cargar los datos JSON
        with open(path_all_projects, 'r', encoding='utf-8') as f:
            all_projects_data = json.load(f)
        with open(path_nasa_tasks, 'r', encoding='utf-8') as f:
            nasa_tasks_data = json.load(f)
    except FileNotFoundError as e:
        st.error(f"Error: No se encontró el archivo {e.filename}. Asegúrate de que 'all_projects.json' y 'nasa_tasks.json' estén en la misma carpeta.")
        return [], [], Config()

    nodes = []
    edges = []
    existing_nodes = set()

    # Procesar all_projects.json
    for project in all_projects_data:
        task_id = project.get('id')
        responsible_center = project.get('project_information', {}).get('responsible_center')
        
        # Nodo para el Task ID
        if task_id and task_id not in existing_nodes:
            nodes.append(Node(id=task_id, label=f"Task: {task_id}", shape="box", color="#FFC75F"))
            existing_nodes.add(task_id)
        
        # Nodo para el Centro Responsable
        if responsible_center and responsible_center not in existing_nodes:
            nodes.append(Node(id=responsible_center, label=responsible_center, shape="ellipse", color="#C34A36"))
            existing_nodes.add(responsible_center)
        
        # Arista entre Task y Centro
        if task_id and responsible_center:
            edges.append(Edge(source=task_id, target=responsible_center, label="managed_by"))

    # Procesar nasa_tasks.json
    for task in nasa_tasks_data:
        task_id = task.get('Task ID')
        pubmed_id = task.get('PubMed ID')
        
        if pubmed_id and pubmed_id != 'No encontrado':
            # Nodo para el PubMed ID
            if pubmed_id not in existing_nodes:
                nodes.append(Node(id=pubmed_id, label=f"PubMed: {pubmed_id}", shape="database", color="#94D2BD"))
                existing_nodes.add(pubmed_id)
            
            # Arista entre Task y PubMed ID
            if task_id:
                # Asegurarse de que el nodo Task ID existe (por si acaso no estaba en all_projects.json)
                if task_id not in existing_nodes:
                    nodes.append(Node(id=task_id, label=f"Task: {task_id}", shape="box", color="#FFC75F"))
                    existing_nodes.add(task_id)
                edges.append(Edge(source=task_id, target=pubmed_id, label="has_publication"))
                
    # Configuración del grafo
    config = Config(width=800,
                    height=600,
                    directed=True,
                    physics=True,
                    hierarchical=False,
                    # Opciones de personalización adicionales
                    nodeHighlightBehavior=True,
                    highlightColor="#F7A7A6",
                    collapsible=True,
                    node={'labelProperty':'label'},
                    link={'labelProperty': 'label', 'renderLabel': True}
                    )

    return nodes, edges, config

def render_configuration_page():

    st.title("Knowledge Graph Grants Projects")
    st.markdown("")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.text_input("Correo Electrónico", value="admin@email.com")
        st.selectbox("Idioma", ["Español", "Inglés"])
        st.button("Guardar Cambios", type="primary")
    with col2:
        #C:\Users\dinho\Desktop\nasa\frontend\RAG\all_proyects.json
        path_all_projects = "RAG/all_proyects.json" 
        path_nasa_tasks = "RAG/taskbook/nasa_tasks.json"
        nodes, edges, config = get_edges_and_nodes(path_all_projects, path_nasa_tasks)
        get_graph(nodes, edges, config)