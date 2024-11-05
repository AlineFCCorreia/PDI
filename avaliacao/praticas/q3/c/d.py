import cv2
import numpy as np
import matplotlib.pyplot as plt

def verificar_direcao(imagem):
    img = cv2.imread(imagem, 0)
    
    # aplicar o filtro Sobel para detectar bordas
    # os gradientes sobel_x e sobel_y, para definir a direção das bordas
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
   
    #achei a tangente do angulos para tentar descobrir a direção
    angulo = np.tan(sobel_y, sobel_x) * (180 / np.pi)  
    
    #contar pixels de acordo com a direção das bordas
    horizontal = np.sum((angulo > -45) & (angulo < 45))     # bordas verticais (orientação horizontal)
    vertical = np.sum((angulo > 45) & (angulo < 135) | (angulo < -45) & (angulo > -135))
      
      
    #visualização
    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)
    plt.subplot(1, 2, 1)
    plt.title("Sobel x")
    plt.imshow(sobel_x, cmap="gray")  
    plt.axis('off')
            
    plt.subplot(1, 2, 2)
    plt.title("Sobel y")
    plt.imshow(sobel_y, cmap="gray")
    plt.axis('off')
    plt.show()
    
    
    if horizontal > vertical:
        direcao = "horizontal"
    elif vertical > horizontal:
        direcao = "vertical"
    else:
        direcao = "inclinada"    
    return f'A direção da ferramenta é {direcao}.'
    
   

imagem = "avaliacao\praticas\q3\CME_01\CME_01_1.jpg"
print(verificar_direcao(imagem))