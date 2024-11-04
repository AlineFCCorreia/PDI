import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d


def carregar(path):
    img = Image.open(path)
    return np.array(img)


def aplicar_filtros(image):
   
    h1 = np.array([1, 1, 1])  
    h2 = np.array([[1], [1], [1]]) 
    
    # Convolução h1 * Im
    filtrado_h1 = convolve2d(image, h1[np.newaxis], mode='same', boundary='wrap')
    
    # Convolução h2 * (h1 * Im)
    filtrado_h2_h1 = convolve2d(filtrado_h1, h2, mode='same', boundary='wrap')
    
    # Convolução (h1 * h2) * Im
    filtro_combinado = convolve2d(h2, h1[np.newaxis], mode='full')
    filtrado_combinado = convolve2d(image, filtro_combinado, mode='same', boundary='wrap')

    
    return filtrado_h2_h1, filtrado_combinado
    

image_path = 'avaliacao\\teorica-pratica\cameraman.bmp' 
imagem = carregar(image_path)

filtrado_h2_h1, filtrado_combinado = aplicar_filtros(imagem)

plt.figure(figsize=(18, 9))

plt.subplot(1, 3, 1)
plt.title("Imagem Original")
plt.imshow(imagem, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Filtragem: h2 * (h1 * Im)")
plt.imshow(filtrado_h2_h1, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Filtragem: (h1 * h2) * Im")
plt.imshow(filtrado_combinado, cmap='gray')
plt.axis('off')

plt.show()
