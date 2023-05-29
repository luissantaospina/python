# Debes encontrar los tres últimos dígitos antes de la coma decimal para (3 + raíz(5)) elevado a n.

# Por ejemplo:
# para n = 5, (3 + √5)5 = 3935.73982... La respuesta es 935.
# Para n = 2, (3 + √5)2 = 27.4164079... La respuesta es 027.

# El primer dato de entrada será la cantidad de valores que se van a analizar.

# Nota: el programa no debe avisar al usuario con mensajes como "Introduzca un número". 
# Debe leer directamente de consola en el formato que se muestra en el apartado "Entradas y salidas de ejemplo". 
# La salida debe ser exactamente como se muestra en ese apartado. El programa debe comportarse bien con valores grandes, 
# de al menos n=30 (sería deseable que también con valores por encima de 1.000.000).

import math

n = input('Ingrese un numero: ')
result = pow((3 + math.sqrt(5)), int(n))
roundNumber = math.trunc(result)
lastThreeDigits = roundNumber % 1000
print(lastThreeDigits)
