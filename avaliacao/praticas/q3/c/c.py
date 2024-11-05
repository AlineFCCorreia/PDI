import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def verificar_borrado(imagem):
    img = cv2.imread(imagem, 0)
    
    # Carregar a imagem 
    img = cv2.imread(imagem, 0)

    # Aplicar o filtro laplaciano, para detectar as bordas
    laplaciano = cv2.Laplacian(img, cv2.CV_64F)
  
    # binarizar a imagem para a posterior con
    _, imagem_bin = cv2.threshold(laplaciano, 50, 255, cv2.THRESH_BINARY)

    # Calcular a soma dos pixels brancos que seriam as bordas
    soma_brancos = np.sum(imagem_bin == 255)
    
    # estou plotando algumas imagens para referência
    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    plt.subplot(1, 3, 1)
    plt.title("Imagem inicial")
    plt.imshow(img, cmap="gray")  
    plt.axis('off')
            
    plt.subplot(1, 3, 2)
    plt.title("Imagem com laplaciano")
    plt.imshow(laplaciano, cmap="gray")
    plt.axis('off')
   
    plt.subplot(1, 3, 3)
    plt.title("Imagem binarizada")
    plt.imshow(imagem_bin, cmap="gray")  
    plt.axis('off')
    
    plt.show()

    # Se a quantidade está baixa, a imagem provavelmente está borrada
    return soma_brancos < 10  


for imagem in os.listdir("avaliacao\praticas\q3\CME_01"):
    caminho_imagem = os.path.join("avaliacao\praticas\q3\CME_01", imagem)
    if verificar_borrado(caminho_imagem):
        print(f"A imagem {imagem} está borrada.")
    