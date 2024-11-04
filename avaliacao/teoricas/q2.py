import math

matrizR = [[255, 240, 200, 150, 120],
        [230, 220, 180, 160, 100],
        [210, 190, 170, 145,  90],
        [170, 160, 140, 130,  80],
        [185, 165, 155, 135, 122]]

matrizG = [[255, 240, 230, 235, 210],
        [240, 245, 250, 255, 180],
        [230, 220,   0, 230, 200],
        [240, 245, 250, 255, 180],
        [255, 240, 230, 235, 210]]

matrizB = [[255,  255,  200,  180,  160],
        [ 240,  230,  190,  140,  120],
        [ 245,  235,    0,  180,  160],
        [ 240,  230,  190,  140,  120],
        [ 255,  255,  200,  180,  160]]



def cinza_media():
    matrizMedia = [[j for j in range(5)] for i in range(5)]
    for lin in range(len(matrizMedia)):
        for col in range(len(matrizMedia[0])):
            matrizMedia[lin][col]= math.ceil((matrizR[lin][col] + matrizG[lin][col] + matrizB[lin][col])/3)
    return matrizMedia

def cinza_pesos():
    #C = 0,29R + 0,59G + 0,11B
    pesoR = 0.29 
    pesoG =  0.59
    pesoB =  0.11

    matrizPesos = [[j for j in range(5)] for i in range(5)]
    for lin in range(len(matrizPesos)):
        for col in range(len(matrizPesos[0])):
            matrizPesos[lin][col]= math.ceil(((matrizR[lin][col])*pesoR) + ((matrizG[lin][col])*pesoG) + ((matrizB[lin][col])*pesoB))
    return matrizPesos
            
print(cinza_media())
print(cinza_pesos())