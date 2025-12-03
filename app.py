import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de Vehículos en EE.UU.')

car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
build_histogram = st.checkbox('Construir Histograma')

if build_histogram:
    st.write('Histograma de Odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox('Construir Gráfico de Dispersión')

if build_scatter:
    st.write('Gráfico de Dispersión: odómetro vs price')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
