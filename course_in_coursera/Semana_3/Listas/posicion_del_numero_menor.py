# Continuemos con la segunda función, en esta tenemos que hallar la posición o
# índice del menor valor dentro de la lista de números


def posicion_del_menor(lista_numeros: list) -> int:
    numero_menor = min(lista_numeros)
    return lista_numeros.index(numero_menor)


numeros = [1, 2, 34, -90, 56, -34, -34, -78]
print(posicion_del_menor(numeros))
