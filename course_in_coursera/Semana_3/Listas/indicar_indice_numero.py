# Escriba una función que reciba una lista y un número entero a buscar, y que retorne
# un entero que indique el índice en que se encuentra este elemento.
#
# En caso de que el elemento se encuentre más de una vez dentro de la lista, debe
# retornar la primera posición en que lo encuentre.
#
# En caso de no encontrar el número, retorne -1.
#
# Nombre de la función: buscar_elemento


def buscar_elemento(lista_numeros: list, numero_buscado: int) -> int:
    posicion_numero_buscado = -1
    if numero_buscado in lista_numeros:
        posicion_numero_buscado = lista_numeros.index(numero_buscado)
    return posicion_numero_buscado


numeros = [1, 2, 34, -90, 56, -34, -34, -78]
numero_a_buscar = int(input('Ingrese el numero a buscar: '))
print(buscar_elemento(numeros, numero_a_buscar))
