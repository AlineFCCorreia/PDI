import numpy as np
from scipy.signal import convolve2d


filtro_box = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

# Máscara do filtro Laplaciano 3x3
filtro_laplaciano = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])


filtro_combinado = convolve2d(filtro_box, filtro_laplaciano, mode='full')
print(filtro_combinado)
