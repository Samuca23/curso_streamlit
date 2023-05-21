import streamlit as st
import yfinance as yf

st.title("Preço de Ativo")
st.header("Informações a respeito do fechamento do volume de algumas ações.")

#ENBR3.SA
#BBAS3.SA
#BBDC4.SA
#PETR4.SA
#VALE5.SA

opcoes = st.selectbox(
    'Escolha o ativo',
    ('ENBR3.SA', 'BBAS3.SA', 'BBDC4.SA', 'PETR4.SA', 'VALE5.SA'))

tickerSimbolo = opcoes
tickerData = yf.Ticker(tickerSimbolo)

tickerDf = tickerData.history(period='1d', start='2013-5-21', end='2023-5-21')

# Open #High #Low #Volume #Dividends #Stock

st.header("Gráfico de fechamento") 
st.line_chart(tickerDf.Close)

st.header("Gráfico de volume")
st.line_chart(tickerDf.Volume)

st.header("Gráfico de dividendos")
st.line_chart(tickerDf.Dividends)