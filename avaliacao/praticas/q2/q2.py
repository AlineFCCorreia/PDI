import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'avaliacao/praticas/q2/alumgrns.bmp' 
image = cv2.imread(path,0) 


#utilizando Canny para detecção de bordas
image_canny = cv2.Canny(image,60,150)

# Fechamento
element = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))
closing = cv2.morphologyEx(image_canny, cv2.MORPH_CLOSE, element) 

# inversão
closing_rev =~ closing

# Erosão, para retirar uma camada extra dos objetos e tornar os contornos mais aparentes
element = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]],dtype=np.uint8)

erode = cv2.erode(closing_rev, element,iterations=1)


plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

plt.subplot(1, 4, 1)
plt.title("Imagem Original")
plt.imshow(image, cmap="gray")  
plt.axis('off')

plt.subplot(1, 4, 2)
plt.title("Imagem com canny")
plt.imshow(image_canny, cmap="gray")  
plt.axis('off')
        
plt.subplot(1, 4, 3)
plt.title("Imagem com fechamento e revertida")
plt.imshow(closing_rev, cmap="gray")
plt.axis('off')


plt.subplot(1, 4, 4)
plt.title("Imagem com erosão")
plt.imshow(erode, cmap="gray")
plt.axis('off')
plt.show()


#utlizando componentes conectados para contar quantas áreas de textura temos
num_labels, img = cv2.connectedComponents(erode)
num_areas = num_labels - 1
print(num_areas)