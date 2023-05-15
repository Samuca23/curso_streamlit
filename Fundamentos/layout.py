import streamlit as st
import numpy as np
import time

st.header("Sidebas")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home page", "Mobile phone")
)

with st.sidebar:
    add_radio = st.radio(
        "choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


st.header("Colunas")
col1, col2 = st.columns(2)

with col1:
    st.header("A cat")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Domestic_White_and_Gray_Cat.JPG/1280px-Domestic_White_and_Gray_Cat.JPG")

with col2:
    st.header("A dog")
    st.image("https://www.dogvibe.com.br/blog/wp-content/uploads/2021/06/guia_racas_golden_retriever_dogvibe.jpg")

st.header("Expander")
st.bar_chart({"data": [1,5,2,6,2,1]})

with st.expander("See explanations"):
    st.write(""" Textttoooo grannndeeee """)
    st.image("https://ceupe.com.ar/blog/wp-content/uploads/2021/04/01-41-1.jpg")


st.header("Container")
with st.container():
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50, 3))
st.write("This is outside the container")


st.header("Empty")
placeholder = st.empty()

placeholder.text("Hello")

placeholder.line_chart({"data": [1, 5, 2, 6]})

with placeholder.container():
    st.write("This is one elment")
    st.write("This is another")

placeholder.empty()