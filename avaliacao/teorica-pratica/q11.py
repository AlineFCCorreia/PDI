import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d
import cv2

# A função filter2D() pode ser utilizada para aplicar o kernel à imagem
# Onde ddepth é a "profundidade" da imagem final. Se ddepth = -1, terá mesma profundidade (x bits) que a imagem de referência.
# prewittH = cv2.filter2D(src=image, ddepth=-1, kernel=h_prewitt)


image_path = "avaliacao\\teorica-pratica\cameraman.bmp"
# imagem = np.array(Image.open(image_path))
imagem = Image.open(image_path).convert("L")  # Converte para escala de cinza
imagem = np.array(imagem, dtype=np.uint16)

# cv2.flip(kernel, -1) convolucao
h1 = np.array([[1, 1, 1]], dtype=np.uint16)
h2 = np.array([[1], [1], [1]], dtype=np.uint16)


# Conrelacao h1 * Im
filtrado_h1 = cv2.filter2D(src=imagem, ddepth=-1, kernel=h1)

# Correlacao h2 * (h1 * Im)
filtrado_h2_h1 = cv2.filter2D(src=filtrado_h1, ddepth=-1, kernel=h2)

# Convolução (h1 * h2) * Im
filtro_combinado = (h2 @ h1) # Produto entre h1 e h2
# filtro_combinado = np.dot(h2, h1)
filtrado_combinado = cv2.filter2D(src=imagem, ddepth=-1, kernel=filtro_combinado)

print(filtro_combinado)
plt.figure(figsize=(18, 9))

plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(imagem, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("Filtrado com h1")
plt.imshow(filtrado_h1, cmap="gray")
plt.axis("off")


plt.subplot(1, 4, 3)
plt.title("Filtragem: h2 * (h1 * Im)")
plt.imshow(filtrado_h2_h1, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.title("Filtragem: (h1 * h2) * Im")
plt.imshow(filtrado_combinado, cmap="gray")
plt.axis("off")

plt.show()
