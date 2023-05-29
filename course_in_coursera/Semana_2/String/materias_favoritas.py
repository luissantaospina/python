# Pedro es un estudiante inteligente pero desinteresado por algunas de sus materias.
# A Pedro le gustan las clases en las que aprende programación, matemática, filosofía y
# literatura. Por lo anterior, cualquier materia que lleve en su título alguna de estas palabras, será de su agrado.
#
# Pedro está planeando su horario, pero ha puesto a su asistente digital a que le dé posibles conjuntos de
# tres materias para inscribir en su semestre. Él quiere saber, dados los títulos de las tres materias,
# cuántas de estas son de su agrado. Se sabe que los nombres de las materias irán sin acentos y en minúsculas
# cuando sean recibidos por parámetro en la función.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: conteo_de_materias
#
# Si lo requiere, puede agregar funciones adicionales.

def conteo_de_materias(materias: list) -> int:
    numero_materias = 0
    for i in materias:
        if i.find('programacion') >= 0 or i.find('matematica') >= 0 \
                or i.find('filosofía') >= 0 or i.find('literatura') >= 0:
                    numero_materias += 1
    return numero_materias


materias = []
for i in range(3):
    materia = input('Ingrese la materia n°' + str(i + 1) + ': ')
    materias.append(materia)

print('El numero de materias que le interesan a Pedro son', conteo_de_materias(materias))
