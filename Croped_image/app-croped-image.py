import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

st.title("Corta Imagem")

img_file = st.sidebar.file_uploader(label="Envie sua Imagem", type=['png', 'jpg'])
realtime_update = st.sidebar.checkbox(label="Atualização em tempo real", value=True)
box_color = st.sidebar.color_picker(label="Grupo de cores", value='#0000FF')
aspect_choice = st.sidebar.radio(label="Proporção da Tela", options=["1:1", "16:9", "4:3"])

aspect_dict = {
    "1:1":(1,1),
    "16:9":(16,9),
    "4:3":(4,3)
}

aspect_ratio = aspect_dict[aspect_choice]

if img_file:
    img = Image.open(img_file)

    if not realtime_update:
        st.write("Duplo click para cortar")
    
    img_cortada = st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)

    st.write("Resultado")
    corte = img_cortada.thumbnail((350, 350))
    st.image(img_cortada)
