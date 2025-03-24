import streamlit as st
import pandas as pd 
import plotly.express as px 

st.set_page_config(layout='wide')


df = pd.read_csv('C:/Users/Caliel/Downloads/dashboard_plotly-main/produtos_servicos.csv', sep=";", decimal=",")
df = df.fillna("Mês sem um novo Estoque")

df["Data de inclusão"] = pd.to_datetime(df["Data de inclusão"])
df=df.sort_values("Data de inclusão")

df["Mês"] = df["Data de inclusão"].apply(lambda x: "Mês " + str(x.month) + " de " + str(x.year))
month = st.sidebar.selectbox("Mês", df["Mês"].unique())

filtrando = df[df["Mês"] == month]
# filtrando

coluna1, coluna2 = st.columns(2)

demanda_mes_barra = px.bar(filtrando, x="Produto", y="Estoque", title="Demanda de Produtos Detalhados")
coluna1.plotly_chart(demanda_mes_barra)

demanda_mes_pizza = px.pie(filtrando, values="Estoque", names="Produto", title="Demanda de Produtos em Porcentagem")
coluna2.plotly_chart(demanda_mes_pizza)
