# Andrés es un profesor que tiene la teoría de que hay filas del salón que tienen mejor promedio que otras.
# Para comprobarlo, ha decidido crear una función que calcule el promedio de la nota de una fila.
# La función recibe como parámetros una matriz, un número de fila y retorna el promedio de la fila redondeado a
# dos decimales. Cuidado: un 0 en la matriz no significa que el estudiante haya sacado 0, sino que
# no hay ningún estudiante en dicha silla.
#
# Tenga muy en cuenta que para Andrés la primera fila es la número 1. Si se pide un número de fila que
# no tenga sentido, su función debe retornar -1. Si la fila no tiene estudiantes, su función debe retornar 0.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: promedio_fila
# Si lo requiere, puede agregar funciones adicionales.


def promedio_fila(salon_a_buscar: list, fila_a_promediar: int) -> float:
    sumatoria_fila = 0
    fila_a_promediar -= 1
    cantidad_estudiantes_en_fila = 0
    if fila_a_promediar >= len(salon_a_buscar) or fila_a_promediar < 0:
        promedio = -1
    else:
        for i in range(len(salon_a_buscar[fila_a_promediar])):
            sumatoria_fila += salon_a_buscar[fila_a_promediar][i]
            if salon_a_buscar[fila_a_promediar][i] != 0:
                cantidad_estudiantes_en_fila += 1
        if cantidad_estudiantes_en_fila > 0:
            promedio = round((sumatoria_fila / cantidad_estudiantes_en_fila), 2)
        else:
            promedio = 0
    return promedio


salon = [
    [5.0, 4.2, 3.5],
    [0, 0, 0],
    [2.0, 0, 3.9],
    [3.0, 3.8, 4.9]
]

fila = 2

print(promedio_fila(salon, fila))
