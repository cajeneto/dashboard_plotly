import streamlit as st
import pandas as pd 
import plotly.express as px 

st.set_page_config(layout='wide')

df = pd.read_csv('produtos_servicos.csv', sep=";", decimal=",", parse_dates=True, dayfirst=True)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_tipo = px.pie(df, names="Tipo", title="Distribuição por tipo de venda")
col1.plotly_chart(fig_tipo)