import streamlit as st
import pandas as pd
import numpy as np

if st.button('Mensage') :
    st.write('Olá Mundo')
else :
    st.write('Adeus')

st.header('Botão Download')

@st.cache
def convert_df(df) :
    return df.to_csv().encode('utf-8')

my_large_df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

st.header("Check Box")
aceito = st.checkbox('Eu aceito os termos')

if aceito :
    st.write('Parabéns')
else :
    st.write('Leia os termos')

st.header('Radio Box')

genero = st.radio('Qual seu gênero favorito', ('Ação', 'Comédia', 'Terror'))

if genero == 'Comédia' :
    st.write('Você selecionou Comédia.')
else : 
    st.write('Você não gosta de filmes de comédia')