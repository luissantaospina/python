# Escriba una función que encuentre el mayor número en una lista de enteros positivos.
#
# En caso de que la lista esté vacía, se debe retornar-1.
#
# Nombre de la función: encontrar_mayor

def encontrar_mayor(lista_numeros: list) -> int:
    mayor = -1
    if lista_numeros:
        mayor = max(lista_numeros)
    return mayor


numeros = [1, 2, 34, -90, 56, -34, -34, -78]
print(encontrar_mayor(numeros))
