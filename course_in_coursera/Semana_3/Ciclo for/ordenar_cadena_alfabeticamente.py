# Escriba una función que reciba una cadena de caracteres (str) por parámetro y retorne dicha cadena
# ordenada alfabéticamente.
#
# Por ejemplo, si se recibe la palabra "bca", el retorno correcto sería "abc".
#
# Suponga que las palabras que su función deberá ordenar están compuestas únicamente del alfabeto inglés
# en minúsculas. La cadena no tiene espacios.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: ordenar_cadena
# Si lo requiere, puede agregar funciones adicionales.


def ordenar_cadena(cadena_a_ordenar: str) -> str:
    return "".join(sorted(cadena_a_ordenar))


cadena = input('Ingrese la cadena a ordenar: ')
print(ordenar_cadena(cadena))
