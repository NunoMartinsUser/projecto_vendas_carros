mport pandas as pd
import streamlit as st
import plotly.express as px


st.header('Carros Vendidos em Portugal')
st.image("https://flagcdn.com/w320/pt.png", width=150)


df = pd.read_csv('carros_europa_combinado.csv')

df_espanha = df[df['País'] == 'Portugal']

st.subheader('🚧 Página em cosntrução 🚧')
with st.expander('Tabela Completa de Portugal'):

    st.dataframe(df_espanha)

df_filtrado = df_espanha.copy()

filtro = [x for x in df_espanha.columns if x not in ['']]

for x in filtro:
    opcoes = ['---Selecionar---'] + sorted(df_filtrado[x].unique().tolist())
    escolha = st.selectbox(f'Selecionar uma opção para {x}', opcoes)
    if escolha != '---Selecionar---':
        df_filtrado = df_filtrado[df_filtrado[x] == escolha]
        st.write(f'Foi selecionado: {escolha}')
