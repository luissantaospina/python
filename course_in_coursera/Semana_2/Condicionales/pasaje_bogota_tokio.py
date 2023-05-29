# Realicemos un ejercicio con algunos condicionales más complejos para seguir reforzando el tema.
# Nos piden crear un programa que permita calcular el valor del pasaje aéreo desde la ciudad de Bogotá hasta Tokio.
# Reproduce el video desde ::23 y sigue la transcripción0:23
# El valor dependerá de una tarifa básica, la compañia aérea elegida para el viaje, la temporada, la edad del
# pasajero y si es o no estudiante. Para calcular el precio, nos dicen que tenemos que tener en cuenta que la
# compañía ALAS incremente el valor de sus pasajes en un 30% en alta temporada, mientras que la compañía VOLAR
# lo incrementa solo en 20%. Ambas compañías descuentan el 50% si el pasajero es menor de edad. Además,
# la compañía VOLAR tiene un recargo de 100.000 pesos para los pasajeros mayores de 60 años para cubrir el
# seguro de vida.
# Reproduce el video desde ::59 y sigue la transcripción0:59
# Los estudiantes que viajan por ALAS y que no son menores de edad tienen un descuento de 10% en temporada baja.
# Y la tarifa básica Bogotá-Tokio reglamentaria es de 5.000.000 de pesos. Para organizar toda esta información y
# poder llegar a una solución adecuada, revisemos primero las entradas, salidas y restricciones o consideraciones a
# tener en cuenta para poder diseñar la solución y posteriormente escribir nuestro código.


def selecciona_aerolinea() -> int:
    valor_aerolinea = 0
    while not valor_aerolinea > 0:
        nivel_actividad_fisica = input('Seleccione la aerolinea'
                                       '\n1: ALAS'
                                       '\n2: VOLAR'
                                       '\n')
        match nivel_actividad_fisica:
            case '1': valor_aerolinea = 1
            case '2': valor_aerolinea = 2
            case _: print('El valor ingresado no es correcto, por favor rectifica')

    return valor_aerolinea


def selecciona_temporada() -> int:
    valor_temporada = 0
    while not valor_temporada > 0:
        nivel_actividad_fisica = input('Seleccione la temporada'
                                       '\n1: Alta'
                                       '\n2: Media'
                                       '\n3: Baja'
                                       '\n')
        match nivel_actividad_fisica:
            case '1': valor_temporada = 1
            case '2': valor_temporada = 2
            case '3': valor_temporada = 3
            case _: print('El valor ingresado no es correcto, por favor rectifica')

    return valor_temporada


def es_estudiante() -> int:
    es_estudiante = 0
    while not es_estudiante > 0:
        nivel_actividad_fisica = input('¿El pasajero es estudiante?'
                                       '\n1: Si'
                                       '\n2: No'
                                       '\n')
        match nivel_actividad_fisica:
            case '1': es_estudiante = 1
            case '2': es_estudiante = 2
            case _: print('El valor ingresado no es correcto, por favor rectifica')

    return es_estudiante


def precio_pasaje(tarifa_basica: int, temporada: int, aerolinea: int, edad: int, es_estudiante: int) -> int:
    seguro_vida = False
    variacion = 0
    if aerolinea == 1 and temporada == 1:
        variacion += 0.3
    elif aerolinea == 2 and temporada == 1:
        variacion += 0.2

    if edad < 18:
        variacion -= 0.5
    elif edad > 60:
        seguro_vida = True

    if es_estudiante == 1 and aerolinea == 1 and edad >= 18 and temporada == 3:
        variacion -= 0.1

    if seguro_vida:
        precio_pasaje = tarifa_basica * variacion + tarifa_basica + 100000
    else:
        precio_pasaje = tarifa_basica * variacion + tarifa_basica

    return int(precio_pasaje)


tarifa_basica = 5000000
temporada = selecciona_temporada()
aerolinea = selecciona_aerolinea()
edad = int(input('Ingrese la edad del pasajero en años: '))
es_estudiante = es_estudiante()

print('El precio del tiquete es', precio_pasaje(tarifa_basica, temporada, aerolinea, edad, es_estudiante), 'COP')
