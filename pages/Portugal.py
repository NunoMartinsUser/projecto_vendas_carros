import pandas as pd
import streamlit as st
import plotly.express as px


st.header('Carros Vendidos em Portugal')
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Flag_of_Portugal_%28official%29.svg/2560px-Flag_of_Portugal_%28official%29.svg.png", width=150)



df = pd.read_csv('venda_carros.csv')

df_espanha = df[df['País'] == 'Portugal']

st.subheader('🚧Página em cosntrução🚧')
with st.expander('Tabela Completa de Portugal'):

    st.dataframe(df_espanha)

df_filtrado = df_espanha.copy()

filtro = [x for x in df_espanha.columns if x not in ['País']]

for x in filtro:
    opcoes = ['---Selecionar---'] + sorted(df_filtrado[x].unique().tolist())
    escolha = st.selectbox(f'Selecionar uma opção para {x}', opcoes)
    if escolha != '---Selecionar---':
        df_filtrado = df_filtrado[df_filtrado[x] == escolha]
        st.write(f'Foi selecionado: {escolha}')
