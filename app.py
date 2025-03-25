import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')

st.header('PROYECTO 7') #TITULO DE LA APP


his_button = st.checkbox('Construir histograma') #BOTÓN 1 HISTOGRAMA
if his_button:
    st.write('Creacion histograma para el conjunto de datos de anuncios de venta de carros')
    fig = px.histogram (car_data , x='odometer')
    st.plotly_chart(fig , user_container_width=True)


dis_button = st.checkbox('Construir diagrama de dispersión') #BOTÓN 2 DISPERSION
if dis_button:
    st.write('Creacion diagrama de dispersion para el conjunto de datos de anuncios de venta de carros')
    fig1 = px.scatter( car_data , y = 'price' , x='odometer')
    st.plotly_chart(fig1 , user_container_width=True)
