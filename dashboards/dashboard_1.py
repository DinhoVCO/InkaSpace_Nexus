# dashboard_1.py (modified to handle internal views)
import streamlit as st
from miscellaneous.d1_main import render_main_content
from miscellaneous.d1_analysis import render_analysis_page
from miscellaneous.d1_configuration import render_configuration_page
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Perfil científico", layout="wide")
st.logo("images/logo_nexus.png", size='large')



import plotly.graph_objects as go

# Estilo: texto grande alineado arriba, como parte de la barra nativa
st.markdown(
    """
    <style>
        .title-navbar {
            font-size: 20px;
            font-weight: 600;
            color: rgb(49, 51, 63);
            margin-top: -60px; /* Lo sube para pegarlo a la barra */
            margin-bottom: 20px;
            padding-left: 15px;
        }

        /* Modo oscuro */
        [data-testid="stAppViewContainer"] {
            background-color: var(--background-color);
        }
        @media (prefers-color-scheme: dark) {
            .title-navbar {
                color: white;
            }
        }
    </style>
    <div class="title-navbar">
        📚 NASA BioScience Dashboard
    </div>
    """,
    unsafe_allow_html=True
)


st.header("🔬 Scientist Dashboard")

def load_sample_data():
    # Datos de ejemplo: reemplaza con la carga real
    data = {
        "id": list(range(1, 21)),
        "titulo": [f"Study {i}" for i in range(1, 21)],
        "anio": [2018,2018,2019,2019,2020,2020,2021,2021,2022,2022,2023,2023,2024,2024,2024,2025,2025,2025,2025,2025],
        "mes": (["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"] * 2)[:20],
        "tema": ["Gene Expression","Microbiome","Plant Growth","Muscle Atrophy","Radiation","Microbiome","Plant Growth","Gene Expression","Microbiome","Radiation","Plant Growth","Muscle Atrophy","Gene Expression","Microbiome","Radiation","Plant Growth","Muscle Atrophy","Gene Expression","Microbiome","Radiation"],
        "organismo": ["Human","Microbe","Plant","Human","Plant","Microbe","Plant","Human","Microbe","Human","Plant","Human","Microbe","Plant","Human","Plant","Human","Microbe","Plant","Human"],
        "autores": ["Smith et al.", "Johnson et al.", "Garcia et al.", "Lee et al.", "Patel et al."]*4,
        "resumen": ["Resumen sintético del artículo..."]*20,
    }
    df = pd.DataFrame(data)
    return df


df = load_sample_data()

with st.sidebar:
    st.subheader("🔎 Filter")
    temas = st.multiselect(
        "Topics", 
        df["tema"].unique(), 
        default=[df["tema"].iloc[0]],
        placeholder="Select a topic"
    )

    organismos = st.multiselect("Organismo(s)", options=sorted(df["organismo"].unique()), default=list(df["organismo"].unique()))
    anios = st.slider("Rango de años", int(df["anio"].min()), int(df["anio"].max()), (int(df["anio"].min()), int(df["anio"].max())))



#aplicar = st.button("Apply")
# Apply filters (reactive)
min_year, max_year = anios


mask = (
    df['tema'].isin(temas) &
    df['organismo'].isin(organismos) &
    (df['anio'] >= min_year) & (df['anio'] <= max_year)
)

df_f = df[mask].copy()
k1, k2, k3, k4 = st.columns(4)

k1.metric("Artículos", len(df_f))
k2.metric("Temas distintos", df_f['tema'].nunique())
k3.metric("Organismos", df_f['organismo'].nunique())
top_author = df_f['autores'].value_counts().idxmax() if not df_f.empty else "-"
k4.metric("Autor más frecuente", top_author)

col_left, col_right = st.columns([6, 3])
with col_left:
    pub_year = df_f.groupby('anio').size().reset_index(name='count')
    st.subheader("Evolución temporal de publicaciones")
    if pub_year.empty:
        st.info("No hay datos para el filtro seleccionado.")
    else:
        fig_time = px.line(pub_year, x='anio', y='count', markers=True)
        st.plotly_chart(fig_time, use_container_width=True)

with col_right:
    st.subheader("Top autores / instituciones")
    top_auth = df_f['autores'].value_counts().reset_index()
    top_auth.columns = ['autor', 'publicaciones']
    st.table(top_auth.head(10))

st.markdown("---")
col_a, col_b = st.columns([2, 3])
#with col_a:
# Tendencias por tema (stacked area)
trend = df_f.groupby(['anio','tema']).size().reset_index(name='count')
st.subheader("Tendencia por tema")
if trend.empty:
    st.write("Sin datos de tendencia.")
else:
    fig_trend = px.area(trend, x='anio', y='count', color='tema', line_group='tema')
    st.plotly_chart(fig_trend, use_container_width=True)

#with col_b:
st.subheader("Listado de artículos (filtrados)")
st.dataframe(df_f[['id','titulo','anio','mes','tema','organismo','autores','resumen']])
