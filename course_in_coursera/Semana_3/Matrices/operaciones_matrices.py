# 1. Tenemos que realizar una función que nos retorne la suma de todos los valores de una matriz
# 2. Suma de una fila dada por parametro
# 3. Suma de una columna dada por parametro
# 4.


def suma_valores_matrices(matriz_a_sumar: list) -> int:
    sumatoria = 0
    for i in range(len(matriz_a_sumar)):
        for j in range(len(matriz_a_sumar[i])):
            sumatoria += matriz_a_sumar[i][j]
    return sumatoria


def suma_fila(matriz_a_sumar: list, fila_a_sumar) -> int:
    sumatoria = 0
    for i in range(len(matriz_a_sumar[fila_a_sumar])):
        sumatoria += matriz_a_sumar[fila_a_sumar][i]
    return sumatoria


def suma_columna(matriz_a_sumar: list, columna_a_sumar) -> int:
    sumatoria = 0
    for i in range(len(matriz_a_sumar)):
        sumatoria += matriz_a_sumar[i][columna_a_sumar]
    return sumatoria


def busca_negativos(matriz_a_sumar: list) -> bool:
    hay_negativos = False
    for i in range(len(matriz_a_sumar)):
        for j in range(len(matriz_a_sumar[i])):
            if matriz_a_sumar[i][j] < 0:
                hay_negativos = True
    return hay_negativos


def busca_fila_con_mas_ceros(matriz_a_sumar: list) -> int:
    fila_ceros = {}
    for i in range(len(matriz_a_sumar)):
        for j in range(len(matriz_a_sumar[i])):
            if matriz_a_sumar[i][j] == 0:
                if not fila_ceros.get(i):
                    fila_ceros[i] = 1
                else:
                    fila_ceros[i] += 1
    mas_ceros = max(fila_ceros.values())
    fila_mas_ceros = list(fila_ceros.keys())[list(fila_ceros.values()).index(mas_ceros)]
    return fila_mas_ceros + 1


matriz = [
    [0,  0, -1, 0],
    [1,  0,  5, 7],
    [9, -6,  0, 0]
]

print('La suma de todos lo valores de la matriz es', suma_valores_matrices(matriz), '\n')

fila = int(input('Ingrese la fila a realizar su sumatoria: '))
print('La suma de todos lo valores de la fila', fila, 'es', suma_fila(matriz, fila - 1), '\n')

columna = int(input('Ingrese la columna a realizar su sumatoria: '))
print('La suma de todos lo valores de la columna', columna, 'es', suma_columna(matriz, columna - 1), '\n')

print('En la matriz hay valores negativos: ', busca_negativos(matriz), '\n')

print('La fila con mas ceros es: ', busca_fila_con_mas_ceros(matriz), '\n')
