import numpy as np
import matplotlib.pyplot as plt

matrizR = np.array([[255, 240, 200, 150, 120],
        [230, 220, 180, 160, 100],
        [210, 190, 170, 145,  90],
        [170, 160, 140, 130,  80],
        [185, 165, 155, 135, 122]], dtype=np.uint8)


matrizG = np.array([[255, 240, 230, 235, 210],
        [240, 245, 250, 255, 180],
        [230, 220,   0, 230, 200],
        [240, 245, 250, 255, 180],
        [255, 240, 230, 235, 210]], dtype=np.uint8)


matrizB = np.array([[255,  255,  200,  180,  160],
        [ 240,  230,  190,  140,  120],
        [ 245,  235,    0,  180,  160],
        [ 240,  230,  190,  140,  120],
        [ 255,  255,  200,  180,  160]], dtype=np.uint8)


imagem_rgb = np.stack((matrizR, matrizG, matrizB), axis=-1)

matriz_media = np.array([[255, 245, 210, 189, 164], 
 [237, 232, 207, 185, 134], 
 [229, 215, 57, 185, 150], 
 [217, 212, 194, 175, 127], 
 [232, 220, 195, 184, 164]]
, dtype=np.float32)

matriz_pesos = np.array([[253, 240, 216, 202, 177], 
 [235, 234, 221, 213, 149],
 [224, 211, 50, 198, 162], 
 [218, 217, 209, 204, 143],
 [233, 218, 203, 198, 177]]
, dtype=np.float32)


plt.figure(figsize=(18, 9))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(imagem_rgb, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Com média")
plt.imshow(matriz_media, cmap="gray")
plt.axis("off")


plt.subplot(1, 3, 3)
plt.title("Com pesos")
plt.imshow(matriz_pesos, cmap="gray")
plt.axis("off")

plt.show()