# Practiquemos el uso de las funciones propias de los strings a través de un ejercicio. Nos piden crear una función
# que nos retorne la cadena con mayor número de a entre cuatro cadenas de caracteres. Tenemos que tener presente
# que debemos contar todas las letras a independiente de si están en mayúscula o minúscula y que en caso de que
# varias cadenas tengan la cantidad mayor de a, debemos retornar la primera de estas


def mas_a(cadenas: list) -> str:
    mayor_a = 0
    cadena_mas_a = ''
    for i in cadenas:
        if i.count('a') > mayor_a:
            mayor_a = i.count('a')
            cadena_mas_a = i
        if i.count('A') > mayor_a:
            mayor_a = i.count('A')
            cadena_mas_a = i
    return cadena_mas_a


cadenas = []
for i in range(4):
    cadena = input('Ingrese la cadena n°' + str(i + 1) + ': ')
    cadenas.append(cadena)

print('La cadena con mas "a" es', mas_a(cadenas))
