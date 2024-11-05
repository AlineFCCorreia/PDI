import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d
import cv2



image_path = "avaliacao\\teorica-pratica\cameraman.bmp"

imagem = Image.open(image_path).convert("L")  # Converte para escala de cinza
imagem = np.array(imagem, dtype=np.uint16)

# Os filtros a serem utilizados
h1 = np.array([[1, 1, 1]], dtype=np.uint16)
h2 = np.array([[1], [1], [1]], dtype=np.uint16)


# Correlacao h1 * Im
# A função filter2D() pode ser utilizada para aplicar o kernel à imagem, fazendo uma correlação cruzada
# Ddepth é a "profundidade" da imagem final. Se ddepth = -1, terá mesma profundidade (x bits) da imagem de referência.
filtrada_h1 = cv2.filter2D(src=imagem, ddepth=-1, kernel=h1)

# Correlacao h2 * (h1 * Im)
filtrada_h2_h1 = cv2.filter2D(src=filtrada_h1, ddepth=-1, kernel=h2)


# Convolução (h1 * h2) * Im
# Nesse caso, a funcao utilizada para convolucao é a convolve2D, mode = full para convolução
filtro_combinado = convolve2d(h2,h1, mode="full")  


filtrada_combinado = cv2.filter2D(src=imagem, ddepth=-1, kernel=filtro_combinado)

print(filtro_combinado)
plt.figure(figsize=(18, 9))

plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(imagem, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("Filtrado com h1")
plt.imshow(filtrada_h1, cmap="gray")
plt.axis("off")


plt.subplot(1, 4, 3)
plt.title("Filtrado com h2 * (h1 * Im)")
plt.imshow(filtrada_h2_h1, cmap="gray")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.title("Filtrado com (h1 * h2) * Im")
plt.imshow(filtrada_combinado, cmap="gray")
plt.axis("off")

plt.show()
