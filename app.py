import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV del conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos')

# Casillas de verificación para gráficos
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma de Odometer")
    
    # Mostrar el gráfico de Plotly
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="model", title="Precio vs. Odometer")
    
    # Mostrar el gráfico de Plotly
    st.plotly_chart(fig_scatter, use_container_width=True)
