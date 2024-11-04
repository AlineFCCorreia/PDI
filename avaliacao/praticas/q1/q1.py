import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'avaliacao\praticas\q1\\tools.bmp'
image = cv2.imread(path,0) 

cv2.imshow("imagem inicial",image )
cv2.waitKey()

_, image_bin = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)
cv2.imshow( "imagem binarizada", ~image_bin)
cv2.waitKey()
image_bin = ~image_bin


element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13)) #


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

img = closing
num_labels, labels = cv2.connectedComponents(img)

print("Número de ferramentas na imagem:", num_labels - 1)