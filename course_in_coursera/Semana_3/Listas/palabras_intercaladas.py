# Queremos poder construir una frase, a partir de dos cadenas, intercalando una palabra de una
# cadena, con una palabra de la otra comenzando con la primera palabra de la primera cadena.
# Por ejemplo, si tenemos las cadenas, la casa está cerca río, y, linda no muy del grande,
# el resultado de la intercalación sería la frase, la linda casa no está muy cerca del río grande.


def devolver_cadena_intercalada(frase_1: str, frase_2: str) -> str:
    lista_palabras_frase_1 = frase_1.split()
    lista_palabras_frase_2 = frase_2.split()
    frase_resultante = ''
    for i in range(0, len(lista_palabras_frase_1)):
        frase_resultante += str(lista_palabras_frase_1[i]) + ' ' + str(lista_palabras_frase_2[i]) + ' '
    return frase_resultante


frase_uno = input('Ingrese la primera frase: ')
frase_dos = input('Ingrese la segunda frase con la misma longitud de la primera: ')

#Ejemplos
# frase_uno = 'la casa está cerca río'
# frase_dos = 'linda no muy del grande'

print(devolver_cadena_intercalada(frase_uno, frase_dos))
