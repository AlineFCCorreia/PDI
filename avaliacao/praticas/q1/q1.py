import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'avaliacao\praticas\q1\\tools.bmp'
image = cv2.imread(path,0) 


#Primeiro, vou binarizar a imagem
_, image_bin = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)


# estou plotando algumas imagens para referência
plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

plt.subplot(1, 2, 1)
plt.title("Imagem inicial")
plt.imshow(image, cmap="gray")  
plt.axis('off')
        
plt.subplot(1, 2, 2)
plt.title("Imagem binarizada")
plt.imshow(image_bin, cmap="gray")
plt.axis('off')
plt.show()


#O inverso da imagem
image_bin = ~image_bin

#elemento estruturante
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13)) #

# aplicando fechamento na imagem, foi visto na monitoria
# uma dilatação seguida de uma erosão, para diminuir as areas em preto, contraí-las
closing = cv2.morphologyEx(image_bin, cv2.MORPH_CLOSE, element) 


plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

plt.subplot(1, 2, 1)
plt.title("Imagem Original")
plt.imshow(image_bin, cmap="gray")  
plt.axis('off')
        
plt.subplot(1, 2, 2)
plt.title("Imagem com fechamento")
plt.imshow(closing, cmap="gray")
plt.axis('off')
plt.show()


#utilizando componentes conectados
img = closing
num_labels, labels = cv2.connectedComponents(img)

#retirando o background da conta
print("Número de ferramentas na imagem:", num_labels - 1)