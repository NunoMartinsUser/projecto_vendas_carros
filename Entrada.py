import streamlit as st
import pandas as pd

st.title("🚗 Vendas de Carros na Europa")

# Carregar dataset (tem de estar no mesmo repositório)
df = pd.read_csv("carros_europa_combinado.csv")

# Mostrar primeiras linhas
st.subheader("Pré-visualização do dataset")
st.dataframe(df.head(10))

