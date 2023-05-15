import streamlit as st
from PIL import Image

st.header("Adicionando Imagem")
image = Image.open('fest.jpg')
st.image(image, caption='festa do chope')

image = Image.open('show.jpg')
st.image(image, caption='festa do chope')

st.header("Áudio")
audio_file = open('teste.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')

st.header("Vídeo")
video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
