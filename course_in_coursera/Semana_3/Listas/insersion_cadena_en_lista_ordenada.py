# Creemos un programa completo que nos permita crear listas ordenadas de "strings".
# Para crear el programa debemos empezar escribiendo una función que reciba por parámetro una
# lista de "strings" que se encuentra ordenada y una cadena para que se inserte dentro de la
# lista de tal forma que se mantenga la lista ordenada. La función, finalmente, debe retornar
# la lista modificada.


def agregar_cadena(lista: list, cadena_a_agregar: str) -> list:
    lista.append(cadena_a_agregar)
    lista.sort()
    return lista


def pedir_items_lista() -> None:
    cadena_a_agregar = ''
    while cadena_a_agregar != 'terminar':
        cadena_a_agregar = input('Ingrese la cadena a agregar: ')
        print(agregar_cadena(lista_ordenada, cadena_a_agregar))


lista_ordenada = []

pedir_items_lista()
