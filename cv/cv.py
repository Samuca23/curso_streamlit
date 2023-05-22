import cv2

def brilho_img(img, resultado):
    img_brilho = cv2.convertScaleAbs(img, beta=resultado)
    return img_brilho

def borra_img(img, resultado):
    img_borra = cv2.GaussianBlur(img, (7,7), resultado)
    return img_borra

def melhora_detalhe(img):
    img_melhorada = cv2.detailEnhance(img, sigma_s=34, sigma_r=0.50)
    return img_melhorada


img = cv2.imread("image/binario.png")

# img_processada = melhora_detalhe(img)
# img_processada = borra_img(img, resultado=35)
img_processada = brilho_img(img, resultado=0.6)

cv2.imshow("Imagem original", img)
cv2.imshow("Imagem processada", img_processada)

cv2.waitKey(0)
cv2.destroyAllWindows()