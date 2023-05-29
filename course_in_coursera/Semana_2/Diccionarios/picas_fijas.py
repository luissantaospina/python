# El juego de las Picas y Fijas es un juego matemático muy sencillo, consiste en adivinar un número de 4
# cifras y de todos los dígitos diferentes. Para esto, el jugador que intenta adivinar deberá decir el
# número que cree está escondiendo el otro, y este deberá responder el número de picas y fijas que tiene
# ahora el jugador.
#
# Una pica es un dígito que se encuentra en el número a adivinar, pero no está en el lugar correcto;
# y una fija es un dígito correctamente colocado.
#
# Por ejemplo, si el número secreto es 1234 y el otro jugador dice 1325, tendrá dos picas y una fija.
#
# Debes crear una función que devuelva un diccionario con las llaves "PICAS" y "FIJAS" que represente
# el resultado de la jugada si un jugador trata de adivinar el numero_secreto con el número intento.
#
# Tu solución debe tener una función de acuerdo con la siguiente especificación:
# Nombre de la función: picas_y_fijas
# Si lo requieres, puedes agregar funciones adicionales.


def picas_y_fijas(numero_intento: int, numero_secreto: int) -> dict:
    cociente_numero_secreto, sobrante_numero_secreto = divmod(numero_secreto, 10)
    cociente_numero_intento, sobrante_numero_intento = divmod(numero_intento, 10)
    if sobrante_numero_secreto == sobrante_numero_intento:
        juego['fijas'] = juego['fijas'] + 1
    cociente_numero_secreto, sobrante_numero_secreto = divmod(cociente_numero_secreto, 10)
    cociente_numero_intento, sobrante_numero_intento = divmod(cociente_numero_intento, 10)
    if sobrante_numero_secreto == sobrante_numero_intento:
        juego['fijas'] = juego['fijas'] + 1
    cociente_numero_secreto, sobrante_numero_secreto = divmod(cociente_numero_secreto, 10)
    cociente_numero_intento, sobrante_numero_intento = divmod(cociente_numero_intento, 10)
    if sobrante_numero_secreto == sobrante_numero_intento:
        juego['fijas'] = juego['fijas'] + 1
    if cociente_numero_secreto == cociente_numero_intento:
        juego['fijas'] = juego['fijas'] + 1
    for i in str(numero_intento):
        if str(numero_secreto).find(str(i)) >= 0:
            juego['picas'] = juego['picas'] + 1
    juego['picas'] = abs(juego['fijas'] - juego['picas'])
    return juego


juego = {
    'picas': 0,
    'fijas': 0
}

secreto = int(input('Ingrese el numero secreto de 4 dígitos: '))
intento = int(input('Ingrese el numero para intentar de 4 dígitos: '))

print(picas_y_fijas(intento, secreto))
