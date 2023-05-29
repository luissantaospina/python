# Los estudiantes de un cierto colegio tienen que ver 5 cursos:
#
# Matemáticas, Español, Ciencias, Literatura y Arte. Usted debe construir una función que
# reciba la información de 5 estudiantes y calcule quién es el mejor estudiante (el que tenga
# el mejor literatura). La información de cada estudiante se representará usando un diccionario con 6
# llaves: "nombre", que tendrá asociado el nombre del estudiante; "matematicas", que tendrá asociada
# la nota del estudiante en el curso Matemáticas; "español", que tendrá asociada la nota del estudiante
# en el curso Español; "ciencias", que tendrá asociada la nota del estudiante en el curso Ciencias;
# "literatura", que tendrá asociada la nota del estudiante en el curso Literatura; y "arte", que tendrá
# asociada la nota del estudiante en el curso Arte. Las notas son números decimales entre 0 y 5.
#
# Su función debe retornar el nombre del estudiante que tenga el mejor literatura. Si hay varios con el mejor
# literatura, debe aparecer el estudiante que tenga el nombre alfabéticamente menor (independientemente de mayúsculas
# o minúsculas).
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: mejor_del_salon
#
# Si lo requiere, puede agregar funciones adicionales.


def crea_estudiante(numero_estudiante: str) -> dict:
    modelo_estudiante['nombre'] = input('Ingrese el nombre del estudiante n°'
                                        + numero_estudiante + ': ')
    modelo_estudiante['matematicas'] = float(input('Ingrese el promedio en matematicas del estudiante n°'
                                                   + numero_estudiante + ': '))
    modelo_estudiante['español'] = float(input('Ingrese el promedio en español del estudiante n°'
                                               + numero_estudiante + ': '))
    modelo_estudiante['ciencias'] = float(input('Ingrese el promedio en ciencias del estudiante n°'
                                                + numero_estudiante + ': '))
    modelo_estudiante['literatura'] = float(input('Ingrese el promedio en literatura del estudiante n°'
                                                  + numero_estudiante + ': '))
    modelo_estudiante['arte'] = float(input('Ingrese el promedio en arte del estudiante n°'
                                            + numero_estudiante + ': '))
    return modelo_estudiante


def mejor_del_salon(lista_estudiantes: list) -> str:
    mejor_estudiante = ''
    mejor_promedio = 0.0
    lista_estudiantes.sort(key=lambda p: p['nombre'])        # Ordena alfabéticamente por nombre
    for estudiante in lista_estudiantes:
        promedio = (estudiante['matematicas'] + estudiante['español'] + estudiante['ciencias']
                    + estudiante['literatura'] + estudiante['arte']) / 5
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_estudiante = estudiante['nombre']
    return mejor_estudiante


modelo_estudiante = {
    'nombre': '',
    'matematicas': 0.0,
    'español': 0.0,
    'ciencias': 0.0,
    'literatura': 0.0,
    'arte': 0.0
}
estudiantes = []

for i in range(5):
    estudiantes.append(crea_estudiante(str(i + 1)))

# Array de estudiantes de ejemplo
# estudiantes = [
#     {
#         'nombre': 'luis',
#         'matematicas': 3.5,
#         'español': 4.5,
#         'ciencias': 3.2,
#         'literatura': 4.8,
#         'arte': 5.0
#     },
#     {
#         'nombre': 'daniela',
#         'matematicas': 3.5,
#         'español': 4.5,
#         'ciencias': 3.2,
#         'literatura': 4.8,
#         'arte': 5.0
#     },
#     {
#         'nombre': 'carlos',
#         'matematicas': 5.0,
#         'español': 4.5,
#         'ciencias': 3.2,
#         'literatura': 4.8,
#         'arte': 5.0
#     },
#     {
#         'nombre': 'andrea',
#         'matematicas': 3.5,
#         'español': 4.5,
#         'ciencias': 3.2,
#         'literatura': 4.8,
#         'arte': 5.0
#     },
#     {
#         'nombre': 'arturo',
#         'matematicas': 3.5,
#         'español': 4.5,
#         'ciencias': 3.2,
#         'literatura': 5.0,
#         'arte': 5.0
#     }
# ]

print(mejor_del_salon(estudiantes))
