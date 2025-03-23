import streamlit as st
import pandas as pd 
import plotly.express as px 

st.set_page_config(layout='wide') # aumentar a tabela para ocupar a tela toda

df = pd.read_csv('produtos_servicos.csv', sep=";", decimal=",")

df

# transforma a coluna "ESTOQUE" para números inteiro. 
df["Estoque"] = pd.to_numeric(df["Estoque"])

# Escolha da categoria
categorias = df["Grupo"].dropna().unique()
categoria_selecionada = st.selectbox("Selecione uma categoria:", options=categorias)

df_filtrado = df[(df["Grupo"] == categoria_selecionada) & (df["Estoque"] < 50)]    

st.markdown("---")
st.markdown(f"### Produtos da categoria: *{categoria_selecionada}* com estoque abaixo de 50")

# Verifica se tem dados
if df_filtrado.empty:
    st.warning("Produto com estoque acima de 50 nesta categoria.")
else:
    fig_dashboard_colunas = px.bar(
        df_filtrado,
        x="Produto",
        y="Estoque",
        color="Produto",
        text="Estoque",
        title=f"Estoque por Produto - {categoria_selecionada}"
    )

    fig_dashboard_colunas.update_traces(textposition='outside')
    fig_dashboard_colunas.update_layout(
        plot_bgcolor='rgba(0,0,5,0)',
        paper_bgcolor='rgba(0,0,5,0)',
        font=dict(size=15),
        title_font_size=20
    )

    st.plotly_chart(fig_dashboard_colunas, use_container_width=True)