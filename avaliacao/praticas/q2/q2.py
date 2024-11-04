import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'avaliacao/praticas/q2/alumgrns.bmp' 
image = cv2.imread(path,0) 

image_canny = cv2.Canny(image,60,150)
cv2.imshow( "imagem com canny", image_canny)
cv2.waitKey()

# Fechamento
element = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15)) #
closing = cv2.morphologyEx(image_canny, cv2.MORPH_CLOSE, element) #image, opening

# inversão
closing_rev =~ closing

cv2.imshow("com fechamento e revertida", closing_rev)
cv2.waitKey()

# Erosão
element = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]],dtype=np.uint8)

erode = cv2.erode(closing_rev, element,iterations=1)

cv2.imshow( "com erosao", erode)
cv2.waitKey()


num_labels, img = cv2.connectedComponents(erode)
num_areas = num_labels - 1
print(num_areas)