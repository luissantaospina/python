# Tus amigos, a quienes también les gusta mucho ver películas, te han propuesto ir al cine la próxima
# semana y quieren conocer los precios de las boletas.
#
# Estas son las tarifas básicas de acuerdo con el tipo de sala:
#
# Dinamix - 18800 pesos
#
# 3D - 15500 pesos
#
# 2D - 11300 pesos.
#
# El cinema tiene, además, varias promociones que aplican para calcular el precio de las boletas que
# dependen del tipo de sala, del número de boletas que se compren simultáneamente, de la hora del día, del
# tipo de pago (tarjeta del cinema u otros medios de pago) y de si se tenía reserva.
#
# Las promociones son las siguientes:
#
# En las horas menos congestionadas (horas no pico) todas las salas tienen un descuento del 10% sobre
# la tarifa básica y si se compran 3 o más boletas, se aplican $500 pesos más de descuento por cada boleta
#
# Si el medio de pago es la tarjeta del cinema, se hace un 5% descuento calculado sobre la tarifa básica
#
# Cuando se hace una reserva, se tiene un recargo de $2000 pesos por boleta sin importar el tipo de sala
#
# En las horas pico, la tarifa básica se incrementa un 25% para las salas 2D y 3D y un 50% para la sala
# Dinamix (este aumento no se tiene en cuenta para los recargos y descuentos).
#
# Debes escribir una función que calcule cuánto te costarán las boletas para ti y tus amigos.


def calcular_costo_boletas(cantidad_boletas: int, tipo_sala: str, hora_pico: bool,
                           pago_tarjeta_cinema: bool, reserva: bool) -> int:
    costo_base = costo_por_sala.get(tipo_sala, 0)
    descuento = 0
    recargo = 0
    if not hora_pico:
        descuento = costo_base * 0.1
        if cantidad_boletas >= 3:
            descuento += cantidad_boletas * 500

    if pago_tarjeta_cinema:
        descuento += costo_base * 0.05

    if reserva:
        recargo = cantidad_boletas * 2000

    if hora_pico and tipo_sala == '2D' or tipo_sala == '3D':
        recargo += costo_base * 0.25

    if hora_pico and tipo_sala == 'Dinamix':
        recargo += costo_base * 0.5

    return round(costo_base + recargo - descuento)


costo_por_sala = {
    'Dinamix': 18800,
    '3D': 15500,
    '2D': 11300
}
cantidad_boletas = 1
tipo_sala = '3D'
hora_pico = False
pago_tarjeta_cinema = True
reserva = False
print(calcular_costo_boletas(cantidad_boletas, tipo_sala, hora_pico, pago_tarjeta_cinema, reserva))
