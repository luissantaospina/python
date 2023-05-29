# Construya una función que reciba como parámetros un texto (cadena de caracteres) y una lista de caracteres
# permitidos (lista de cadenas de caracteres), y que retorne un diccionario con información sobre las palabras
# contenidas en el texto.
#
# La función debe construir un diccionario en el que las llaves son todas las palabras que aparecen en el
# texto, ignorando si en el texto aparecen en mayúsculas o minúsculas. Sin embargo, las llaves del
# diccionario deben ser sólo cadenas en minúscula.
#
# Cada una de las llaves, debe tener asociada una tupla con tres valores de tipo entero: el primero
# indica la cantidad de veces que aparece la palabra en el texto, el segundo indica la primera posición
# en la que aparece la palabra, y el tercero indica la última posición en la que aparece. Si la palabra
# aparece una sola vez en el texto, el segundo y el tercer valor serán iguales.
#
# La lista de caracteres permitidos indica qué caracteres pueden hacer parte de las palabras, cualquier
# carácter que no haga parte de esta lista debe tratarse como si fuera un espacio o un signo de puntuación.
#
# Nota: las posiciones hacen referencia a las posiciones en el texto original que la función recibe como
# parámetro, contadas desde 0.
#
# Veamos un ejemplo en el que los caracteres permitidos son todos los caracteres del español, incluyendo
# las vocales acentuadas. Suponga que el texto que se va a analizar es el siguiente: "Muchos años después, " \
#                                                                                    "" \
#                                                                                    "frente al pelotón de " \
#                                                                                    "fusilamiento, el coronel " \
#                                                                                    "Aureliano Buendía había de " \
#                                                                                    "recordar aquella tarde " \
#                                                                                    "remota en que su padre " \
#                                                                                    "lo llevó a conocer el hielo."
#
# En el diccionario resultante deben aparecer las siguientes palabras, de las cuales sólo dos se repiten:
# 'a', 'al', 'aquella', 'aureliano','años', 'buendía', 'conocer', 'coronel', 'de', 'después', 'el', 'en','frente',
# 'fusilamiento', 'había', 'hielo', 'llevó', 'lo', 'muchos', 'padre', 'pelotón', 'que', 'recordar', 'remota',
# 'su', 'tarde'.
#
#  La palabra 'el' aparece dos veces en el texto, la primera a partir de la posición 56 y la segunda a partir
# de la posición 159. Tenga cuidado, la aparición de la cadena 'el' dentro de la palabra 'hielo' no se tiene en
# cuenta porque no es una palabra completa.
#
# La otra palabra que se repite en este texto es la palabra 'de', que aparece a partir de las posiciones 39 y
# 91. Tenga cuidado de no contar la aparición de la sílaba 'de' en la palabra 'después'.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: analizar_texto
#
# Si lo requiere, puede agregar funciones adicionales.


def normalizar_texto(texto_a_anormalizar: str, caracteres_permitidos_a_validar: list) -> str:
    texto_normalizado = texto_a_anormalizar.lower()
    texto_normalizado = texto_normalizado.replace('.', ' ')
    texto_normalizado = texto_normalizado.replace(',', ' ')
    texto_normalizado = texto_normalizado.replace(';', ' ')
    for letra in texto_normalizado:
        if letra not in caracteres_permitidos_a_validar:
            texto_normalizado = texto_normalizado.replace(letra, ' ')
    print(texto_a_anormalizar)
    print(texto_normalizado)
    return texto_normalizado


def contar_numero_apariciones_palabra(lista_palabras: list, palabra_a_buscar: str) -> int:
    numero_apariciones = 0
    for palabra in lista_palabras:
        if palabra == palabra_a_buscar:
            numero_apariciones += 1
    return numero_apariciones


def encontrar_posicion_inicial_palabra(texto_a_buscar: str, palabra_a_buscar_posicion: str) -> int:
    palabra_completa = ' ' + palabra_a_buscar_posicion + ' '
    posicion = texto_a_buscar.lower().find(palabra_completa)
    return posicion + 1


def encontrar_posicion_final_palabra(texto_a_buscar: str, palabra_a_buscar_posicion: str) -> int:
    palabra_completa = ' ' + palabra_a_buscar_posicion + ' '
    posicion = texto_a_buscar.lower().rfind(palabra_completa)
    return posicion + 2


def analizar_texto(texto_a_validar: str, caracteres_permitidos_a_validar: list) -> dict:
    texto_normalizado = normalizar_texto(texto_a_validar, caracteres_permitidos_a_validar)
    lista_palabras = sorted(texto_normalizado.split())
    resultado = {}
    for palabra in lista_palabras:
        resultado[palabra] = (contar_numero_apariciones_palabra(lista_palabras, palabra),
                              encontrar_posicion_inicial_palabra(texto_normalizado, palabra),
                              encontrar_posicion_final_palabra(texto_normalizado, palabra))
    return resultado


caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é',
                         'í', 'ó', 'ú', 'ñ']
texto = 'Seis suecos sosos secan sesos sin sal, Secan seis sesos los suecos, ' \
        'Salan seis sesos con sal, secan y salan los sesos, que sacan del secadal.'
print(analizar_texto(texto, caracteres_permitidos))
