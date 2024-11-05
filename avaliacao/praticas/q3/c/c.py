import cv2
import numpy as np
import os

def verificar_borrado(imagem):
    img = cv2.imread(imagem, 0)
    
    # Aplicar o filtro Sobel para detectar bordas
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    #calcular a magnitude das bordas
    mag_borda = np.sqrt(sobel_x**2 + sobel_y**2)
    
    #calcular a média das intensidades das bordas
    media_borda = np.mean(mag_borda)
    print(media_borda)
    
    # Se a média é baixa, a imagem provavelmente está borrada
    return media_borda < 10  # Experimental


for imagem in os.listdir("avaliacao\praticas\q3\CME_01"):
    caminho_imagem = os.path.join("avaliacao\praticas\q3\CME_01", imagem)
    if verificar_borrado(caminho_imagem):
        print(f"A imagem {imagem} está borrada.")
    