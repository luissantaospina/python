# # letra TODO: analizar
# def fun(palabra):
#     respuesta = ''
#     contador = 0
#     for letra_actual in palabra:
#         contador_actual = 0
#         for letra in palabra:
#             if letra == letra_actual:
#                 contador_actual += 1
#         if contador < contador_actual:
#             respuesta = letra_actual
#             contador = contador_actual
#     return respuesta
#
#
# print(fun('vesuvius'))
#
#
# # Invertir palabra
# def invertir(palabra):
#     respuesta = ""
#     i = 0
#     while i < len(palabra):
#         respuesta += palabra[len(palabra)-1-i]
#         i += 1
#     return respuesta
#
#
# print(invertir('MISO Virtual'))


# Ordena listas en forma ascendente
# def ordenar(lista):
#     n = len(lista)
#     i = 0
#     while i < n:
#         j = 0
#         while j < (n - i - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#             j += 1
#         i += 1
#     return lista
#
#
# print(ordenar([5, 10, 7]))
import string


def busqueda(letra):
    alfabeto = string.ascii_uppercase
    encontrado = False
    inicio = 0
    final = len(alfabeto) - 1
    while not encontrado:
        mitad = (final + inicio) // 2
        if mitad < 0:
            encontrado = True
            indice = -1
        elif alfabeto[mitad] == letra:
            encontrado = True
            indice = mitad
        elif alfabeto[mitad] < letra:
            inicio = mitad + 1
        else:
            final = mitad - 1
    return indice


busqueda('Z')
