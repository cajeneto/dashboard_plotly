import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Estoque",
    page_icon="📦",
    layout="wide"
)

df = pd.read_csv("produtos_servicos.csv", sep=';')

# Melhora leitura do título
st.markdown("""
    <div style="background-color:#4CAF50;padding:15px;border-radius:10px">
        <h2 style="color:white;text-align:center;">📦 Dashboard de Estoque de Produtos</h2>
    </div>
""", unsafe_allow_html=True)






# -------------- LUIZ LUNA ------------------------

fig_tipo = px.pie(df, names="Tipo", title="Distribuição por tipo de venda")
st.plotly_chart(fig_tipo, use_container_width=True)






# ------------------ HOSTÍLIO NETO -------------------------




# transforma a coluna "ESTOQUE" para números inteiro. 
df["Estoque"] = pd.to_numeric(df["Estoque"])

# Escolha da categoria
categorias = df["Grupo"].dropna().unique()
categoria_selecionada = st.selectbox("Selecione uma categoria:", options=categorias, key='categoria_acima_50')

df_filtrado = df[(df["Grupo"] == categoria_selecionada) & (df["Estoque"] > 50)]    

# st.markdown("---")
st.markdown(f"### Produtos da categoria: **{categoria_selecionada}** com estoque acima de 50")

# Verifica se tem dados
if df_filtrado.empty:
    st.warning("Nenhum produto com estoque abaixo de 50 nesta categoria.")
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

    st.markdown("#### 📋 Tabela de Dados")
    st.dataframe(df_filtrado, use_container_width=True)
st.markdown("---")

#  ------------------- RAFAELA URTIGA -------------------------

# Escolha da categoria
categorias = df["Grupo"].dropna().unique()
categoria_selecionada = st.selectbox("Selecione uma categoria:", options=categorias, key='categoria_abaixo_50')

df_filtrado = df[(df["Grupo"] == categoria_selecionada) & (df["Estoque"] < 50)]    

# st.markdown("---")
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
st.markdown("---")




#  -------------- CALIEL ------------------------

