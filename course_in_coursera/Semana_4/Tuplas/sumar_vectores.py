# Construya una función que reciba dos vectores (con 3 componentes cada uno) y retorne un nuevo
# vector que sea la suma de los dos vectores recibidos. Cada vector debe recibirse como una tupla
# con tres valores flotantes.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: suma_vectorial


def suma_vectorial(vector_1_a_sumar: tuple, vector_2_a_sumar: tuple) -> tuple:
    suma_vectores = (vector_1_a_sumar[0] + vector_2_a_sumar[0],
                     vector_1_a_sumar[1] + vector_2_a_sumar[1],
                     vector_1_a_sumar[2] + vector_2_a_sumar[2]
                     )
    return suma_vectores


vector_1 = (2, 3, 1)
vector_2 = (4, 5, 6)

print(suma_vectorial(vector_1, vector_2))
