# Queremos crear un programa que pida al usuario un número entero n para crear una matriz identidad,
# es decir, una matriz que tiene unos en la diagonal principal y ceros en el resto de celdas, de tamaño n por n


def crea_matriz_identidad(dimension_matriz: int) -> list:
    matriz = []
    for i in range(dimension_matriz):
        matriz.append([0] * dimension_matriz)
        matriz[i][i] = 1
    return matriz


dimension = int(input('Ingrese la dimensión: '))
matriz_identidad = crea_matriz_identidad(dimension)

for fila in matriz_identidad:
    print(fila)
