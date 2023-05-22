import cv2
import streamlit as st
import numpy as np
from PIL import Image
from skimage import morphology, io, color, feature, filters

def principal():
    st.title("OpenCV App")
    st.subheader("Aplicativo para integrar processamentos de imagens com OpenCV")
    
    file_img = st.file_uploader("Envia sua imagem", type=["jpg", "png", "jpeg"])

    taxa_borrao = st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5)
    qnt_brilho = st.sidebar.slider("Brilho", min_value=50, max_value=50, value=0)
    melhoramento = st.sidebar.checkbox("Melhorar detalhes")
    cinza = st.sidebar.checkbox("Converter para escala cinza")
    img_erosao = st.sidebar.checkbox("Aplicar filtro Erosão")
    img_dilatacao = st.sidebar.checkbox("Aplicar filtro Dilatação")
    img_edge = st.sidebar.checkbox("Aplicar filtro Edge")
    
    
    
    if not file_img:
          return None
    
    img_original = Image.open(file_img)
    img_original = np.array(img_original)
    img_processada = borra_img(img_original, taxa_borrao)
    img_processada = brilho_img(img_processada,qnt_brilho)
    
    if (melhoramento):
         img_processada = melhora_detalhe(img_processada)

    if (cinza):
        img_processada = escala_cinza(img_processada)
    
    if (img_erosao):
        img_processada = morphology.erosion(img_processada)

    if (img_dilatacao):
        img_processada = morphology.dilation(img_processada)

    if (img_edge):
        img_processada = filters.sobel(img_processada)

    st.text("Imagem Original")
    st.image(img_original)

    st.text("Imagem Processada")
    st.image(img_processada)
    
def brilho_img(img, resultado):
    img_brilho = cv2.convertScaleAbs(img, beta=resultado)
    return img_brilho

def borra_img(img, resultado):
    img_borra = cv2.GaussianBlur(img, (7,7), resultado)
    return img_borra

def melhora_detalhe(img):
    img_melhorada = cv2.detailEnhance(img, sigma_s=34, sigma_r=0.50)
    return img_melhorada

def escala_cinza(img):
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_cinza

if __name__ == '__main__':
        principal()
