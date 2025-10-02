import streamlit as st
import pandas as pd
import numpy as np

def render_analysis_page():
    """Muestra el contenido de la página de Análisis de Datos."""
    st.title("📊 Análisis de Datos")
    st.markdown("Esta página muestra gráficos y tablas interactivas.")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Ventas', 'Costos', 'Beneficios'])
    st.line_chart(chart_data)
    st.dataframe(chart_data)