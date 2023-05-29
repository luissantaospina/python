# Seguro que has visto textos como "The quick brown fox jumps over the lazy dog" o 
# "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el
# saxofón detrás del palenque de paja" .
# Son "pangramas", textos que contienen todas las letras de un cierto alfabeto, quizá repetidas.

# Deberás crear un programa que reciba varias frases y que diga si cada una de ellas es un pangrama o no. 
# Sólo deberás considerar las letras del alfabeto inglés (no te preocupes por
# las vocales acentuadas ni la eñe, entre otras),
# que podrán aparecer en mayúsculas o en minúsculas.

# La primera línea contendrá el número de frases y después aparecerá una nueva frase en cada línea. 
# Para cada frase deberás responder SI cuando se trate de un pangrama o NO cuando no lo sea.

import string

alphabetLower = list(string.ascii_lowercase)
alphabetUpper = list(string.ascii_uppercase)
sentence = input('Ingrese una frase: ')
matchCounter = 0

for i in sentence:
    for j in alphabetLower:
        if i == j:
            alphabetLower.remove(j)
            alphabetUpper.remove(j.upper())
            matchCounter += 1

    for k in alphabetUpper:
        if i == k:
            alphabetUpper.remove(k)
            alphabetLower.remove(k.lower())
            matchCounter += 1
            
if matchCounter == 26:
    print('Si')
else:
    print('No')
