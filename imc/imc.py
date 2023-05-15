import streamlit as st

st.title("Calculadora IMC")

peso = st.number_input("Digite seu peso (em KG)")

status = st.radio("Selecione a opção de Altura",
                  ("cm", "m"))

if status == 'cm':
    altura = st.number_input("Digite a altura em centímetros")
    try:
        imc = peso / ((altura / 100) **2)
    except:
        st.error("Insire algum valor de altura")
else:
    altura = st.number_input("Digita a altura em metros")
    try:
        imc = peso / (altura **2)
    except:
        st.error("Insira algum valor de altura")

if altura and peso:
    if(st.button("Calcular IMC")):
        st.text("Seu índice de IMC é: {}".format(imc))

    if(imc < 16):
        st.error("Você está extremamente abaixo do peso")
    elif(imc >= 16 and imc < 18.5):
        st.warning("Abaixo do peos")
    elif(imc >= 18.5 and imc < 25):
        st.success("Saudável")
    elif(imc >=25 and imc < 30):
        st.warning("Excesso de peso")
    elif(imc <=30):
        st.error("Extramamente acima do peso")
        
