import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def render_analysis_page():
    #st.header("🔬 Scientist Dashboard")
    st.logo("images/logo_nexus.png", size='large')
    st.set_page_config(page_title="Perfil científico", layout="wide")

    # NEW
    import json

    from pathlib import Path

    # ---------- FUNCIONES AUXILIARES ----------
    def load_json(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        return data

    def extract_field(d, key):
        """Extrae campos de un dict anidado, si existen."""
        if isinstance(d, dict):
            return d.get(key)
        return None

    # ---------- CARGA DE DATOS ----------
    metadata = load_json("metadata.json")
    projects = load_json("all_proyects.json")
    tasks = load_json("nasa_tasks.json")

    # ---------- DATAFRAME ARTÍCULOS ----------
    df_articles = pd.DataFrame([
        {
            "pmcid": k,
            "title": v.get("title"),
            "authors": v.get("authors"),
            "date": v.get("publication_date")
        }
        for k, v in metadata.items()
    ])
    df_articles["date"] = pd.to_datetime(df_articles["date"], errors="coerce")
    df_articles["year"] = df_articles["date"].dt.year
    df_articles["month"] = df_articles["date"].dt.month

    # ---------- DATAFRAME PROYECTOS ----------
    df_projects = pd.DataFrame(projects)
    df_projects["start_date"] = pd.to_datetime(df_projects["start_date"], errors="coerce")
    df_projects["end_date"] = pd.to_datetime(df_projects["end_date"], errors="coerce")
    df_projects["year"] = df_projects["start_date"].dt.year
    df_projects["responsible_center"] = df_projects["project_information"].apply(lambda x: extract_field(x, "responsible_center"))
    df_projects["project_type"] = df_projects["project_information"].apply(lambda x: extract_field(x, "project_type"))
    df_projects["discipline"] = df_projects["research_discipline_element"].fillna("").str.extract(r"Division:(.*)$", expand=False)

    # ---------- DATAFRAME NASA TASKS ----------
    df_tasks = pd.DataFrame(tasks)
    df_tasks["PI Name"] = df_tasks["PI Name"].fillna("Unknown")

    # ---------- CONFIGURACIÓN STREAMLIT ----------
    st.set_page_config(page_title="NASA Space Biology Dashboard", layout="wide")
    st.title("🧬 Scientist Dashboard")

    st.subheader("🔎 Filter")
    



    # ---- Filtros adicionales ----
    centers = sorted(df_projects["responsible_center"].dropna().unique())
    types = sorted(df_projects["project_type"].dropna().unique())
    disciplines = sorted(df_projects["discipline"].dropna().unique())

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        selected_centers = st.multiselect("Responsible Center", centers)
    with col2:
        selected_types = st.multiselect("Project Type", types)
    with col3:
        selected_disciplines = st.multiselect("Discipline", disciplines)
    with col4:
        # ---- Filtro por rango de años ----
        min_year = int(df_articles["year"].min())
        max_year = int(df_articles["year"].max())
        year_range = st.slider(
            "Select a range of years",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year)
        )

    # ---------- APLICAR FILTROS ----------
    filtered_articles = df_articles[
        (df_articles["year"] >= year_range[0]) &
        (df_articles["year"] <= year_range[1])
    ]

    filtered_projects = df_projects.copy()
    if selected_centers:
        filtered_projects = filtered_projects[filtered_projects["responsible_center"].isin(selected_centers)]
    if selected_types:
        filtered_projects = filtered_projects[filtered_projects["project_type"].isin(selected_types)]
    if selected_disciplines:
        filtered_projects = filtered_projects[filtered_projects["discipline"].isin(selected_disciplines)]

    # ---------- TABS PRINCIPALES ----------
    tab1, tab2, tab3 = st.tabs(["📈 Research Timeline", "🏗️ Project Distribution", "👩‍🔬 Researchers"])

    # ---------- TAB ARTÍCULOS ----------
    with tab1:
        st.subheader("Evolution of scientific publications")

        col1, col2 = st.columns(2)

        with col1:
            yearly_counts = filtered_articles.groupby("year").size().reset_index(name="count")
            fig_year = px.bar(
                yearly_counts, x="year", y="count", text="count",
                title="Number of articles per year"
            )
            st.plotly_chart(fig_year, use_container_width=True)

        with col2:
            monthly_counts = filtered_articles.groupby(["year", "month"]).size().reset_index(name="count")
            fig_month = px.line(
                monthly_counts, x="month", y="count", color="year",
                title="Monthly distribution of publications"
            )
            st.plotly_chart(fig_month, use_container_width=True)

        st.dataframe(filtered_articles[["year", "title", "authors"]].sort_values(by="year", ascending=False))

    # ---------- TAB PROYECTOS ----------
    with tab2:
        st.subheader("NASA Project Statistics")

        col1, col2 = st.columns(2)

        with col1:
            center_counts = filtered_projects["responsible_center"].value_counts().reset_index()
            center_counts.columns = ["Center", "Quantity"]
            fig_center = px.bar(center_counts, x="Center", y="Quantity",
                                title="Projects by responsible center", text="Quantity")
            st.plotly_chart(fig_center, use_container_width=True)

        with col2:
            type_counts = filtered_projects["project_type"].value_counts().reset_index()
            type_counts.columns = ["Project Type", "Quantity"]
            fig_type = px.pie(type_counts, values="Quantity", names="Project Type",
                            title="Types of NASA projects")
            st.plotly_chart(fig_type, use_container_width=True)

        st.subheader("Distribution by discipline")

        # Contar ocurrencias y asegurar nombres consistentes
        disc_counts = (
            filtered_projects["discipline"]
            .dropna()
            .value_counts()
            .reset_index()
        )

        # Renombrar columnas de forma segura
        disc_counts.columns = ["Discipline", "Quantity"]

        # Asegurar que las columnas existan
        if "Discipline" in disc_counts.columns and "Quantity" in disc_counts.columns:
            fig_disc = px.bar(
                disc_counts.sort_values("Quantity", ascending=True),
                x="Quantity",
                y="Discipline",
                orientation="h",
                text="Quantity",
                title="Projects by discipline"
            )

            fig_disc.update_traces(textposition="outside")
            fig_disc.update_layout(
                yaxis=dict(tickfont=dict(size=11)),
                xaxis_title="Number of projects",
                yaxis_title="Scientific discipline",
                margin=dict(l=200, r=40, t=60, b=40),
                height=600,
            )

            st.plotly_chart(fig_disc, use_container_width=True)
        else:
            st.warning("No disciplinary data was found to graph.")


    # ---------- TAB INVESTIGADORES ----------
    with tab3:
        st.subheader("Most productive principal investigators (PIs)")

        pi_counts = df_tasks["PI Name"].value_counts().reset_index()
        pi_counts.columns = ["PI Name", "Publications"]

        fig_pi = px.bar(
            pi_counts.head(20),
            x="PI Name",
            y="Publications",
            text="Publications",
            title="Top 20 Researchers with the Most Publications NASA"
        )
        st.plotly_chart(fig_pi, use_container_width=True)

        st.dataframe(pi_counts, use_container_width=True)

    # ---------- PIE DE PÁGINA ----------
    st.markdown("---")
    st.caption("🛰️ Source: NASA OSDR, Task Book, Space Biology Publications (2025).")



