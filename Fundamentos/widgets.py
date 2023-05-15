import streamlit as st
import pandas as pd
import numpy as np
import datetime

from io import StringIO

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


st.header("CheckBox")
aceito = st.checkbox('Eu aceito os termos')

if aceito :
    st.write('Parabéns')
else :
    st.write('Leia os termos')


st.header('RadioBox')
genero = st.radio('Qual seu gênero favorito', ('Ação', 'Comédia', 'Terror'))

if genero == 'Comédia' :
    st.write('Você selecionou Comédia.')
else : 
    st.write('Você não gosta de filmes de comédia')


st.header("SelectBox")
opcao = st.selectbox('Escolha a opçaõ de contato', ('Email', 'Telefone'))

if opcao == 'Email' :
    st.write('Você selecionou Email')
else :
    st.write('Você seleciou Telefone')


st.header("Utilizando multiselect")
opcoes = st.multiselect('Quais suas cores favoritas?', ('Preto', 'Azul', 'Verde', 'Rosa'))


st.header("Utilizadno o Slider")
idade = st.slider('Quanto anos você tem?', 0, 100, 25)
st.write("Eu tenho ", idade, ' anos de idade')


st.header("Utilizando o Select Slider")
colors = st.select_slider("Selecione uma cor",
                          options=['red', 'orange', 'black', 'white'] )
st.write('Minha cor favorita é ', colors)


st.header("Utilizando Input Text")
title = st.text_input('Movie Title', 'Life od Brian')
st.write('The current movie title is', title)


st.header("Utilizando Input Number")
number = st.number_input("Insert a number")
st.write('The current number is', number)


st.header("Utilizando Text Area")
text_area = st.text_area('Text to analyze', ''' aaaa muito texxtooo''')
st.write('Texto: ', text_area)

st.header('Utilizando Input Date')
d = st.date_input('Selecione seu aniversários',
                     datetime.date(2019, 7, 6))
st.write('Seu aniversário é: ', d)


st.header("Input Time")
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarme para ', t)


st.header('Input File')
uploaded_file = st.file_uploader('Chooser a file')
if uploaded_file is not None :
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    string_data = stringio.read()
    st.write(string_data)

    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


st.header("Input Camera")
picture = st.camera_input("Take a Picture")
if picture :
    st.image(picture)


st.header("Color Picker")

color = st.color_picker('Pick a color')
st.write('The current Color is', color)