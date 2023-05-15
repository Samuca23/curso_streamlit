import streamlit as st
import pandas as pd
import numpy as np

st.header("Utilizando DataFrame")
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(df)

st.header("Utilizadno Table")
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)
st.table(df)

st.header("Utilizando métrica")
st.metric(label= "Temperatura", value="70 ºF", delta="1.2 ºF")

st.header("Utilizando JSON")
st.json({
    'foo' : 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

