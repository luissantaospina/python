# Practiquemos el uso de diccionarios con un ejercicio para ver algunas ventajas que nos brinda
# esta estructura. Nos solicitan contar la cantidad de ocurrencias o veces que aparece cada uno de
# los dígitos del cero al nueve dentro de un numero de diez cifras. Por ejemplo, para el número
# que vemos en pantalla nuestro programa debe informar que el ocho aparece tres veces, el tres
# aparece una vez, el cuatro aparece dos veces, el siete aparece una vez, el dos aparece dos veces
# y el nueve aparece una vez. Para solucionar el problema podemos utilizar un diccionario como un
# histograma you que estaremos contando las ocurrencias o frecuencia de cada uno de los dígitos
# dentro del número de diez cifras que representaría nuestro conjunto de datos. Siguiendo esta idea,
# los dígitos del cero al nueve que aparezcan en el número serán las claves o llaves en nuestro diccionario,
# mientras que las veces que aparece cada uno serán los valores.


def obtener_numero_repeticiones(numero_usuario: int) -> None:
    for key, value in numeros.items():
        for i in str(numero_usuario):
            if key == int(i):
                numeros[key] = numeros[key] + 1


numeros = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

numero = int(input('Ingrese un numero: '))

obtener_numero_repeticiones(numero)
print(numeros)
