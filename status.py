import streamlit as st
import time

st.header("Barra de progresso")
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)


st.header("Spinner")

with st.spinner("Wait for it..."):
    time.sleep(5)
    st.success("Done!")


st.header("Ballons")
st.balloons()

st.header("Snowflake")
st.snow()


st.header("Mensagens")
st.warning("Cuidade, isso é uma aviso!")
st.success("Deu boa, sucesso!")
st.error("Deu ruim, erro!")
st.info("This is a purely information message")

a = RuntimeError("This is an exception of type RuntimeError")
st.exception(a)