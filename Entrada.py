import pandas as pd
import streamlit as st
import plotly.express as px


st.header('Carros Vendidos na Europa')

df = pd.read_csv('venda_carros.csv')


# filtros = df.columns.difference(["Preço (€)", "Quilometragem (km)"]).tolist()
filtros = [col for col in df.columns if col not in [
    'País', "Preço (€)", "Tipo"]]

df_filtrado = df.copy()

for coluna in filtros:
    opcoes = ['-- Selecione um valor --'] + \
        sorted(df_filtrado[coluna].unique().tolist())
    escolha = st.selectbox(f"Escolha {coluna}", opcoes)

    if escolha != '-- Selecione um valor --':
        df_filtrado = df_filtrado[df_filtrado[coluna] == escolha]
        st.write(f"{coluna} selecionado foi: {escolha}")

if not df_filtrado.equals(df):

    df_grouped = (df_filtrado.groupby(
        'País').size().reset_index(name='Número de Carros'))

    fig1 = px.bar(df_grouped, x='País', y='Número de Carros', color='País',
                  title='Número de carros vendidos por país de acordo com os filtos selecionados')

    st.plotly_chart(fig1, use_container_width=True)

    with st.expander('Tabela Completa Filtrada'):

        st.dataframe(df_filtrado)
