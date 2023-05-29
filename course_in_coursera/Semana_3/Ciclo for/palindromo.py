# Tenemos que escribir una función que nos diga si una cadena de caracteres es palíndromo, es decir,
# si es una palabra o frase que se lee de igual manera de izquierda a derecha que de derecha a izquierda.
# Por ejemplo, tenemos las frases "Isaac no ronca así" o "Sometamos o matemos". Pasemos a Spyder para ver
# la implementación


def normalizar(frase_a_normalizar: str) -> str:
    frase_normalizada = frase_a_normalizar.lower()
    frase_normalizada = frase_normalizada.replace(' ', '')
    acentos = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'E': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }
    for acento in acentos:
        if acento in frase_normalizada:
            frase_normalizada = frase_normalizada.replace(acento, acentos[acento])
    return frase_normalizada


def buscar_palindromo(frase_a_analizar: str) -> bool:
    es_palindromo = False
    frase_reversa = ''
    for i in frase_a_analizar:
        frase_reversa = i + frase_reversa
    if frase_reversa == frase_a_analizar:
        es_palindromo = True
    return es_palindromo


frase = input('Ingrese la frase: ')
print(buscar_palindromo(normalizar(frase)))
