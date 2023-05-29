#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Billboard.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos

@author: Cupi2
"""
import billboard as bb


def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")
    canciones = bb.cargar_canciones(archivo)
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo", archivo)
    return canciones


def ejecutar_buscar_cancion(canciones: list) -> None:
    """ Ejecuta la opción de buscar una canción dado el nombre y el año del 
    ranking al cual pertenece 
    """
    cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = int(input("Por favor ingrese el año de la canción que desea buscar: "))
    print(bb.buscar_cancion(canciones, cancion, anio))


def ejecutar_buscar_canciones_anio(canciones: list) -> None:
    """ Ejecuta la opción de consultar las canciones de un año dado 
    """
    anio = int(input("Por favor ingrese el año que desea consultar: "))
    print(bb.buscar_canciones_anio(canciones, anio))


def ejecutar_buscar_canciones_artista_periodo(canciones: list) -> None:
    """ Ejecuta la opción de consultar las canciones de un artista dado en 
    un periodo de tiempo definido 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inicio = int(input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))
    print(bb.buscar_canciones_artista_periodo(canciones, artista, anio_inicio, anio_fin))


def ejecutar_buscar_canciones_artista(canciones: list) -> None:
    """ Ejecuta la opción de consultar todas las canciones de un artista dado 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    print(bb.buscar_canciones_artista(canciones, artista))


def ejecutar_buscar_todos_artistas_cancion(canciones: list) -> None:
    """ Ejecuta la opción de consultar todos los artistas que han interpretado 
    una canción dada 
    """
    cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    print(bb.buscar_todos_artistas_cancion(canciones, cancion))


def ejecutar_buscar_artistas_mas_populares(canciones: list) -> None:
    """ Ejecuta la opción de consultar los artistas más populares 
    """
    minimo = int(input("Por favor ingrese la cantidad mínima de canciones que desea buscar: "))
    print(bb.buscar_artistas_mas_populares(canciones, minimo))


def ejecutar_buscar_artista_estrella(canciones: list) -> None:
    """ Ejecuta la opción de consultar el artista estrella de todos los tiempos 
    """
    print(bb.buscar_artista_estrella(canciones))


def ejecutar_buscar_artistas_y_sus_canciones(canciones: list) -> None:
    """ Ejecuta la opción de consultar la lista completa de artistas del Billboard 
    junto con sus canciones 
    """
    print(bb.buscar_artistas_y_sus_canciones(canciones))


def ejecutar_calcula_promedio_canciones_por_artista(canciones: list) -> None:
    """ Ejecuta la opción de consultar la cantidad promedio de canciones que los 
    artistas tienen en el listado de Billboard 
    """
    print(bb.calcula_promedio_canciones_por_artista(canciones))

    
def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")    
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = input("Por favor seleccione una opción: ")
        match opcion_seleccionada:
            case '1': canciones = ejecutar_cargar_canciones()
            case '2': ejecutar_buscar_cancion(canciones)
            case '3': ejecutar_buscar_canciones_anio(canciones)
            case '4': ejecutar_buscar_canciones_artista_periodo(canciones)
            case '5': ejecutar_buscar_canciones_artista(canciones)
            case '6': ejecutar_buscar_todos_artistas_cancion(canciones)
            case '7': ejecutar_buscar_artistas_mas_populares(canciones)
            case '8': ejecutar_buscar_artista_estrella(canciones)
            case '9': ejecutar_buscar_artistas_y_sus_canciones(canciones)
            case '10': ejecutar_calcula_promedio_canciones_por_artista(canciones)
            case '11': continuar = False
            case _: print("La opción " + opcion_seleccionada + " no es valida.")


iniciar_aplicacion()
