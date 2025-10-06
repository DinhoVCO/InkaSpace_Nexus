import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px

def render_analysis_page():
    st.logo("images/logo_nexus.png", size='large')
    st.set_page_config(page_title="Profile Architec", layout="wide")
    def load_json(path):
        with open(path, "r") as f:
            return json.load(f)

    def extract_field(d, key):
        if isinstance(d, dict):
            return d.get(key)
        return None

    # Load JSON files
    metadata = load_json("metadata.json")
    projects = load_json("all_proyects.json")
    tasks = load_json("nasa_tasks.json")

    # ------------------ Prepare Data ------------------
    # Articles
    df_articles = pd.DataFrame([
        {"pmcid": k, "title": v.get("title"), "date": v.get("publication_date")}
        for k, v in metadata.items()
    ])
    df_articles["date"] = pd.to_datetime(df_articles["date"], errors="coerce")
    df_articles["year"] = df_articles["date"].dt.year

    # Projects
    df_projects = pd.DataFrame(projects)
    df_projects["start_date"] = pd.to_datetime(df_projects["start_date"], errors="coerce")
    df_projects["end_date"] = pd.to_datetime(df_projects["end_date"], errors="coerce")
    df_projects["year"] = df_projects["start_date"].dt.year
    df_projects["responsible_center"] = df_projects["project_information"].apply(lambda x: extract_field(x, "responsible_center"))
    df_projects["project_type"] = df_projects["project_information"].apply(lambda x: extract_field(x, "project_type"))
    df_projects["discipline"] = df_projects["research_discipline_element"].fillna("").str.extract(r"Division:(.*)$", expand=False)

    # Tasks
    df_tasks = pd.DataFrame(tasks)
    df_tasks["PI Name"] = df_tasks["PI Name"].fillna("Unknown")

    # ------------------ Streamlit Setup ------------------
    st.set_page_config(page_title="Space Biology — Mission Architect View", layout="wide")
    st.title("👷🏻‍♂️ Mission Architect Dashboard")

    st.subheader("🔎 Filters")

    
    # Responsible centers & project types
    centers = sorted(df_projects["responsible_center"].dropna().unique())
    types = sorted(df_projects["project_type"].dropna().unique())
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_centers = st.multiselect("Responsible Center", centers)
    with col2:
        selected_types = st.multiselect("Project Environment (Type)", types)
    with col3:
        # Year range filter
        min_year = int(df_articles["year"].min())
        max_year = int(df_articles["year"].max())
        year_range = st.slider(
            "Select Year Range",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year)
        )


    # Apply filters
    filtered_articles = df_articles[
        (df_articles["year"] >= year_range[0]) &
        (df_articles["year"] <= year_range[1])
    ]

    filtered_projects = df_projects.copy()
    if selected_centers:
        filtered_projects = filtered_projects[filtered_projects["responsible_center"].isin(selected_centers)]
    if selected_types:
        filtered_projects = filtered_projects[filtered_projects["project_type"].isin(selected_types)]

    # ------------------ Tabs ------------------
    tab1, tab2, tab3 = st.tabs([
        "📈 Research Timeline",
        "🏗️ Project Distribution",
        "👩‍🔬 Researchers"
    ])

    # ---------- TAB 1: Publications ----------
    with tab1:
        st.subheader("Research Activity Over Time")

        yearly_counts = filtered_articles.groupby("year").size().reset_index(name="Count")
        fig_pub = px.bar(
            yearly_counts,
            x="year",
            y="Count",
            text="Count",
            title="Publications per Year"
        )
        fig_pub.update_traces(textposition="outside")
        fig_pub.update_layout(
            xaxis_title="Year",
            yaxis_title="Number of Publications",
            height=500
        )
        st.plotly_chart(fig_pub, use_container_width=True)

    # ---------- TAB 2: Projects ----------
    with tab2:
        st.subheader("Project Distribution by Environment and Center")

        col1, col2 = st.columns(2)

        # --- Project type (environment) ---
        with col1:
            type_counts = (
                filtered_projects["project_type"]
                .dropna()
                .value_counts()
                .reset_index()
            )
            type_counts.columns = ["Project Type", "Count"]

            fig_env = px.pie(
                type_counts,
                values="Count",
                names="Project Type",
                title="Project Environment Distribution"
            )
            fig_env.update_traces(textinfo="percent+label", textposition="inside")
            st.plotly_chart(fig_env, use_container_width=True)

        # --- Responsible center ---
        with col2:
            center_counts = (
                filtered_projects["responsible_center"]
                .dropna()
                .value_counts()
                .reset_index()
            )
            center_counts.columns = ["Responsible Center", "Count"]

            fig_center = px.bar(
                center_counts.sort_values("Count", ascending=True),
                x="Count",
                y="Responsible Center",
                orientation="h",
                text="Count",
                title="Projects by Responsible Center"
            )
            fig_center.update_traces(textposition="outside")
            fig_center.update_layout(margin=dict(l=200, r=40, t=60, b=40))
            st.plotly_chart(fig_center, use_container_width=True)

        # --- Project timeline ---
        st.subheader("Project Initiation Timeline")
        timeline_counts = filtered_projects.groupby("year").size().reset_index(name="Count")
        fig_timeline = px.line(
            timeline_counts,
            x="year",
            y="Count",
            markers=True,
            title="Projects Initiated per Year"
        )
        fig_timeline.update_layout(
            xaxis_title="Start Year",
            yaxis_title="Number of Projects",
            height=400
        )
        st.plotly_chart(fig_timeline, use_container_width=True)

    # ---------- TAB 3: Scientific Focus ----------
    with tab3:
        st.subheader("Leading Biological Disciplines")

        disc_counts = (
            filtered_projects["discipline"]
            .dropna()
            .value_counts()
            .reset_index()
        )
        disc_counts.columns = ["Discipline", "Count"]

        fig_disc = px.bar(
            disc_counts.sort_values("Count", ascending=True),
            x="Count",
            y="Discipline",
            orientation="h",
            text="Count",
            title="Projects by Scientific Discipline"
        )
        fig_disc.update_traces(textposition="outside")
        fig_disc.update_layout(
            margin=dict(l=200, r=40, t=60, b=40),
            height=600,
            xaxis_title="Number of Projects",
            yaxis_title="Discipline"
        )
        st.plotly_chart(fig_disc, use_container_width=True)

    # ---------- Footer ----------
    st.markdown("---")
    st.caption("🛰️ Data Source: OSDR, Task Book, and Space Biology Publications (2025).")