import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
#conf  pag
st.set_page_config(page_title='exploratory', page_icon=':bar_chart:',layout='wide')

st.title('Curso de Machine Learning - UPDS')
# subtitulo
st.subheader('Analisis exploratorio')

st.markdown('## Normalizacion de Datos')

# agregar sidebar
st.sidebar.title('Description')

#agregar una lista de modelos de regresion

st.sidebar.markdown('## modelos de regresion')
st.sidebar.markdown('- reg lineal')
st.sidebar.markdown('- reg logistica')
st.sidebar.markdown('- Regresion Polinomial')

st.sidebar.markdown('## Modelos Supervisado')
model=st.sidebar.selectbox('selecciones un modelo',['Regresion Lineal','Regresion Logistica','Regresion polinomial'])

#lista paises
paises=['bolvia','Argentina','Brasil','Chile','Paraguay']

#agregar un select multiple
st.sidebar.markdown('## Paises')
paises_selec=st.sidebar.multiselect('Seleccione los paises',paises)

# slider de años desde 200 hasta 2024
st.sidebar.markdown('## Años')
año=st.sidebar.slider('Seleccione un año',2000,2024,2020)

# cargar 
