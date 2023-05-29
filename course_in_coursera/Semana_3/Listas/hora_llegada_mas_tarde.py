# Ahora nos piden escribir una función que retorne el vuelo que llega más tarde.
# Veamos de nuevo qué estrategia seguir para la solución, para luego proceder al código.
# Lo primero será poder comparar dos horas de llegada. Para esto, necesitaremos otra función.
# Y empezamos comparando las horas de los dos tiempos. Si alguna es mayor que la otra,
# si las horas serán iguales, debemos comparar los minutos. Y si alguna es mayor,
# you tenemos nuestra respuesta. De nuevo, si los minutos serán iguales, toca comparar los segundos,
# y si alguna es mayor sabremos cuál de los dos tiempos es mayor. En caso de ser iguales,
# también significaría que ambos tiempos son exactamente iguales. La función nos retornará
# entonces 0 si ambos tiempos comparados son iguales, 1 si el primero es mayor al segundo,
# y menos 1 en caso contrario. Finalmente, la solución a encontrar el vuelo que llega más
# tarde consistirá en recorrer la lista de vuelos, comparando las horas de llegada que
# obtenemos al invocar la función que hicimos como solución al primer problema, para buscar
# el mayor usando el algoritmo de búsqueda secuencial que hemos visto en el curso para hallar el mayor.


def calcula_llega_mas_tarde(lista_vuelos: list) -> int:
    vuelo_mas_tarde = 0
    if lista_vuelos[0]['hora_llegada'] > lista_vuelos[1]['hora_llegada']:
        vuelo_mas_tarde = 1
    elif lista_vuelos[0]['hora_llegada'] < lista_vuelos[1]['hora_llegada']:
        vuelo_mas_tarde = -1

    elif lista_vuelos[0]['minuto_llegada'] > lista_vuelos[1]['minuto_llegada']:
        vuelo_mas_tarde = 1
    elif lista_vuelos[0]['minuto_llegada'] < lista_vuelos[1]['minuto_llegada']:
        vuelo_mas_tarde = -1

    elif lista_vuelos[0]['segundo_llegada'] > lista_vuelos[1]['segundo_llegada']:
        vuelo_mas_tarde = 1
    elif lista_vuelos[0]['segundo_llegada'] < lista_vuelos[1]['segundo_llegada']:
        vuelo_mas_tarde = -1

    return vuelo_mas_tarde


vuelos = [
    {
        'hora_llegada': 20,
        'minuto_llegada': 15,
        'segundo_llegada': 56
    },
    {
        'hora_llegada': 20,
        'minuto_llegada': 16,
        'segundo_llegada': 56
    }
]

print(calcula_llega_mas_tarde(vuelos))
