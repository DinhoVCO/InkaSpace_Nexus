import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px

def render_analysis_page():
    st.logo("images/logo_nexus.png", size='large')
    st.set_page_config(page_title="Perfil científico", layout="wide")

    # ------------------ Load JSON data ------------------
    def load_json(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        return data

    def extract_field(d, key):
        if isinstance(d, dict):
            return d.get(key)
        return None

    metadata = load_json("metadata.json")
    projects = load_json("all_proyects.json")
    tasks = load_json("nasa_tasks.json")

    # ------------------ Data Preparation ------------------
    # Articles
    df_articles = pd.DataFrame([
        {
            "pmcid": k,
            "title": v.get("title"),
            "date": v.get("publication_date")
        }
        for k, v in metadata.items()
    ])
    df_articles["date"] = pd.to_datetime(df_articles["date"], errors="coerce")
    df_articles["year"] = df_articles["date"].dt.year
    df_articles["month"] = df_articles["date"].dt.month

    # Projects
    df_projects = pd.DataFrame(projects)
    df_projects["start_date"] = pd.to_datetime(df_projects["start_date"], errors="coerce")
    df_projects["end_date"] = pd.to_datetime(df_projects["end_date"], errors="coerce")
    df_projects["year"] = df_projects["start_date"].dt.year
    df_projects["responsible_center"] = df_projects["project_information"].apply(lambda x: extract_field(x, "responsible_center"))
    df_projects["project_type"] = df_projects["project_information"].apply(lambda x: extract_field(x, "project_type"))
    df_projects["discipline"] = df_projects["research_discipline_element"].fillna("").str.extract(r"Division:(.*)$", expand=False)

    # Tasks (PI)
    df_tasks = pd.DataFrame(tasks)
    df_tasks["PI Name"] = df_tasks["PI Name"].fillna("Unknown")

    # ------------------ Streamlit Layout ------------------
    st.set_page_config(page_title="NASA Space Biology Dashboard - Manager", layout="wide")
    st.title("💼 Manager Dashboard")


    # Year range filter
    min_year = int(df_articles["year"].min())
    max_year = int(df_articles["year"].max())
    
    
    st.subheader("🔎 Filters")
    # Additional filters
    centers = sorted(df_projects["responsible_center"].dropna().unique())
    types = sorted(df_projects["project_type"].dropna().unique())

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_centers = st.multiselect("Responsible Center", centers)
    with col2:
        selected_types = st.multiselect("Project Type", types)
    with col3:
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
        "👩‍🔬 Researchers"])

    # ---------- TAB 1: Publications ----------
    with tab1:
        st.subheader("Publications Overview")

        col1, col2 = st.columns(2)

        with col1:
            yearly_counts = filtered_articles.groupby("year").size().reset_index(name="count")
            fig_year = px.bar(
                yearly_counts,
                x="year",
                y="count",
                text="count",
                title="Publications per Year"
            )
            fig_year.update_traces(textposition="outside")
            st.plotly_chart(fig_year, use_container_width=True)

        with col2:
            monthly_counts = filtered_articles.groupby(["year", "month"]).size().reset_index(name="count")
            fig_month = px.line(
                monthly_counts,
                x="month",
                y="count",
                color="year",
                markers=True,
                title="Monthly Publication Trend"
            )
            st.plotly_chart(fig_month, use_container_width=True)

    # ---------- TAB 2: Projects ----------
    with tab2:
        st.subheader("Project Statistics")

        col1, col2 = st.columns(2)

        with col1:
            center_counts = (
                filtered_projects["responsible_center"]
                .dropna()
                .value_counts()
                .reset_index()
            )
            # Asegurar nombres correctos de columnas
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
            fig_center.update_layout(
                margin=dict(l=200, r=40, t=60, b=40),
                yaxis=dict(tickfont=dict(size=11)),
                xaxis_title="Number of Projects",
                yaxis_title="Responsible Center"
            )
            st.plotly_chart(fig_center, use_container_width=True)

        with col2:
            # Count project types and ensure consistent column names
            type_counts = (
                filtered_projects["project_type"]
                .dropna()
                .value_counts()
                .reset_index()
            )
            type_counts.columns = ["Project Type", "Count"]

            # Create pie chart safely
            fig_type = px.pie(
                type_counts,
                values="Count",
                names="Project Type",
                title="Project Type Distribution"
            )

            fig_type.update_traces(textposition="inside", textinfo="percent+label")
            fig_type.update_layout(
                showlegend=True,
                height=500,
                margin=dict(l=40, r=40, t=60, b=40)
            )

            st.plotly_chart(fig_type, use_container_width=True)

        st.subheader("Projects by Start Year")
        timeline_counts = filtered_projects.groupby("year").size().reset_index(name="count")
        fig_timeline = px.bar(
            timeline_counts,
            x="year",
            y="count",
            text="count",
            title="Projects Initiated per Year"
        )
        fig_timeline.update_traces(textposition="outside")
        st.plotly_chart(fig_timeline, use_container_width=True)

    # ---------- TAB 3: Researchers ----------
    with tab3:
        st.subheader("Top Principal Investigators (PIs)")

        pi_counts = df_tasks["PI Name"].value_counts().reset_index()
        pi_counts.columns = ["PI Name", "Publications"]

        fig_pi = px.bar(
            pi_counts.head(20).sort_values("Publications", ascending=True),
            x="Publications",
            y="PI Name",
            orientation="h",
            text="Publications",
            title="Top 20 PIs by Publications"
        )
        fig_pi.update_traces(textposition="outside")
        fig_pi.update_layout(margin=dict(l=200, r=40, t=60, b=40))
        st.plotly_chart(fig_pi, use_container_width=True)

    # ---------- Footer ----------
    st.markdown("---")
    st.caption("🛰️ Data sources: NASA OSDR, Task Book, and Space Biology Publications (2025).")