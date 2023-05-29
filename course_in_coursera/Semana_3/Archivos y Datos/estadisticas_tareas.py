# Como parte de una iniciativa de analítica sobre el desempeño de los estudiantes para
# identificar las dificultades que tienen en un curso, se recopilaron las notas que
# obtuvieron en diferentes tareas. Ahora, queremos analizarlas con un pequeño programa
# que usted tendrá que construir.
#
# La información obtenida está organizada en un diccionario donde las llaves son los
# nombres de los estudiantes (cadenas de caracteres) y los valores son diccionarios.
#
# En estos diccionarios "internos", las llaves son los nombres de las tareas y los
# valores son las notas obtenidas por el estudiante para esa tarea (un número entero
# entre 0 y 100).
#
# Es decir, si el único estudiante en la muestra se llama "Roberto" y ha realizado dos
# tareas ("Tarea 1" y "Tarea 2" con notas de 80 y 90 respectivamente), el diccionario
# de diccionarios con esta información se vería en Python de la siguiente forma:
# {"Roberto": {"Tarea 1": 80, "Tarea 2" : 90}}.
#
# Tenga cuidado: no todos los estudiantes resolvieron todas las tareas.
#
# Usted debe construir una función que, dados los resultados de los estudiantes,
# calcule las siguientes estadísticas para una tarea dada su nombre: la mayor nota obtenida,
# el nombre del estudiante que obtuvo la mejor nota, la menor nota obtenida, el nombre del
# estudiante que obtuvo la peor nota, el promedio de las notas de los estudiantes,
# la cantidad de estudiantes que recibieron una nota y la suma de las notas obtenidas por los estudiantes.
#
# La función debe retornar un diccionario con las siguientes llaves: "mayor", "mejor", "menor",
# "peor", "promedio", "cantidad" y "total".
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
# Nombre de la función: calcular_estadisticas_tarea
# Si lo requiere, puede agregar funciones adicionales.


def calcula_mejor_nota_estudiante_total(lista_estudiantes: dict) -> dict:
    mejor_nota = {
        'mayor': 0,
        'mejor': ''
    }
    for key, value in lista_estudiantes.items():
        if max(value.values()) > mejor_nota['mayor']:
            mejor_nota['mayor'] = max(value.values())
            mejor_nota['mejor'] = key
    return mejor_nota


def calcula_peor_nota_estudiante_total(lista_estudiantes: dict) -> dict:
    peor_nota = {
        'menor': 100,
        'peor': ''
    }
    for key, value in lista_estudiantes.items():
        if min(value.values()) < peor_nota['menor']:
            peor_nota['menor'] = min(value.values())
            peor_nota['peor'] = key
    return peor_nota


def calcula_mejor_nota_estudiante(lista_estudiantes: dict, tarea_a_buscar: str) -> dict:
    mejor_nota = {
        'mayor': 0,
        'mejor': ''
    }
    for key, value in lista_estudiantes.items():
        if value.get(tarea_a_buscar) and value.get(tarea_a_buscar) > mejor_nota['mayor']:
            mejor_nota['mayor'] = value.get(tarea_a_buscar)
            mejor_nota['mejor'] = key
    return mejor_nota


def calcula_peor_nota_estudiante(lista_estudiantes: dict, tarea_a_buscar: str) -> dict:
    peor_nota = {
        'menor': 100,
        'peor': ''
    }
    for key, value in lista_estudiantes.items():
        if value.get(tarea_a_buscar) and value.get(tarea_a_buscar) < peor_nota['menor']:
            peor_nota['menor'] = value.get(tarea_a_buscar)
            peor_nota['peor'] = key
    return peor_nota


def calcula_promedio_notas(lista_estudiantes: dict, tarea_a_buscar: str) -> dict:
    tarea = {
        'promedio': 0,
        'cantidad': 0,
        'total': 0
    }
    for key, value in lista_estudiantes.items():
        if value.get(tarea_a_buscar):
            tarea['total'] += value.get(tarea_a_buscar)
            tarea['cantidad'] += 1
    tarea['promedio'] = tarea['total'] / tarea['cantidad']
    return tarea


def calcular_estadisticas_tarea(lista_estudiantes: dict, tarea_a_buscar: str) -> dict:
    estadisticas = calcula_mejor_nota_estudiante(lista_estudiantes, tarea_a_buscar)
    estadisticas.update(calcula_peor_nota_estudiante(lista_estudiantes, tarea_a_buscar))
    estadisticas.update(calcula_promedio_notas(lista_estudiantes, tarea_a_buscar))
    return estadisticas


estudiantes = {
    'luis': {
        'tarea 1': 90,
        'tarea 2': 90,
        'tarea 3': 60,
        'tarea 4': 90
    },
    'daniel': {
        'tarea 1': 50,
        'tarea 2': 98,
        'tarea 4': 60
    },
    'andres': {
        'tarea 2': 5
    },
    'luisa': {
        'tarea 1': 90,
        'tarea 2': 90,
        'tarea 3': 60,
        'tarea 4': 90
    },
    'daniela': {
        'tarea 1': 50,
        'tarea 2': 98,
        'tarea 4': 60,
        'tarea 5': 90
    },
    'andrea': {
        'tarea 3': 95,
        'tarea 4': 60
    }
}
tarea = 'tarea 2'
print(calcular_estadisticas_tarea(estudiantes, tarea))
