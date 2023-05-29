# Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso. 
# Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio
# entre cada pareja de palabras.
# La salida debe ser "Case #" seguido del número de caso, 
# de un símbolo de "dos puntos", de un espacio en blanco y de la frase invertida.

numberSentences = int(input('Ingrese el numero de frases a revertir: '))
sentences = []
sum = ''
iterator = 1

for i in range(numberSentences):
    sentence = input('Ingrese la frase n°' + str(i + 1) + ': ')
    sentences.append(sentence)

for j in sentences:
    splitSentence = j.split()
    for k in splitSentence:
        sum = k + ' ' + sum

    print('Caso n°' + str(iterator) + ': ' + sum)
    sum = ''
    iterator += 1
