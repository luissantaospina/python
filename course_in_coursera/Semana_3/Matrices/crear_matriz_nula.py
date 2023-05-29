

def crea_matriz_nula(filas: int, columnas: int) -> list:
    matriz = []
    for _ in range(filas):
        matriz.append([0] * columnas)
    return matriz


numero_filas = int(input('Ingrese el numero de filas: '))
numero_columnas = int(input('Ingrese el numero de columnas: '))

print(crea_matriz_nula(numero_filas, numero_columnas))
