# Una clase de la Universidad de los Andes tiene las siguientes reglas con
# respecto a las aproximaciones de las notas finales.
#
# Si la nota es mayor o igual a 4.5, la nota se aproxima a 5.0.
# Si la nota es mayor o igual a 3.5 y menor a 4.5, la nota se aproxima a 4.0.
# Si la nota es mayor o igual a 2.5 y menor a 3.5, la nota se aproxima a 3.0.
# De lo contrario, la nota asignada será 1.5.
#
# Teniendo una lista de diccionarios en donde cada uno corresponde a un estudiante
# y que tiene como llaves "nombre" y "nota" (sin aproximar), retorne una lista con todos
# los diccionarios actualizados con sus notas después de aproximación.
#
# Cada uno de los diccionarios retornados tiene las llaves "nombre" y "nota"(aproximada).
#
# Se garantiza que la lista tiene al menos un diccionario.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: calcular_definitivas
# Si lo requiere, puede agregar funciones adicionales.


def calcular_definitivas(lista_estudiantes: list) -> list:
    for estudiante in lista_estudiantes:
        if estudiante['nota'] >= 4.5:
            estudiante['nota'] = 5.0
        elif 3.5 <= estudiante['nota'] < 4.5:
            estudiante['nota'] = 4.0
        elif 2.5 <= estudiante['nota'] < 3.5:
            estudiante['nota'] = 3.0
        else:
            estudiante['nota'] = 1.5
    return lista_estudiantes


estudiantes = [
    {
        'nombre': 'luis',
        'nota': 4.6
    },
    {
        'nombre': 'juan',
        'nota': 3.6
    },
    {
        'nombre': 'dani',
        'nota': 2.6
    },
    {
        'nombre': 'dani',
        'nota': 1.8
    }
]

print(calcular_definitivas(estudiantes))
