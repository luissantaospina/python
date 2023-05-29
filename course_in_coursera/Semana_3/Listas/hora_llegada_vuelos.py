# La secretaria de una agencia de vuelos necesita poder informar a los clientes
# la hora de llegada de sus vuelos. Para poder determinar esto, conoce la hora de
# salida de los vuelos en horas, minutos y segundos, y la duración de cada vuelo,
# también en horas, minutos y segundos. Como ejemplo, podemos tomar un vuelo que
# parte a las 11, 48, con 10 segundos, con una duración de 2 horas, 11 minutos y 58
# segundos. Así que estará llegando a las 14 horas, 0 minutos, 8 segundos. Podemos
# suponer que todos los vuelos llegan el mismo día en que parten. Debemos escribir
# entonces una función que reciba una lista de diccionarios donde cada uno contiene
# la información de un vuelo que es hora de partida y duración, y retorne otra lista
# de diccionarios con la hora de llegada de cada uno


def calcula_hora_llegada(lista_vuelos: list) -> list:
    for vuelo in lista_vuelos:
        horas_llegada = 0
        minutos_llegada = 0
        segundos_llegada = vuelo['segundos_partida'] + vuelo['segundos_duracion']
        if segundos_llegada > 60:
            segundos_llegada -= 60
            minutos_llegada += 1
        minutos_llegada += vuelo['minutos_partida'] + vuelo['minutos_duracion']
        if minutos_llegada > 60:
            minutos_llegada -= 60
            horas_llegada += 1
        horas_llegada += vuelo['horas_partida'] + vuelo['horas_duracion']
        vuelo['hora llegada'] = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(horas_llegada, minutos_llegada, segundos_llegada)

    return lista_vuelos


vuelos = [
    {
        'horas_partida': 10,
        'minutos_partida': 20,
        'segundos_partida': 11,
        'horas_duracion': 1,
        'minutos_duracion': 30,
        'segundos_duracion': 45
    },
    {
        'horas_partida': 20,
        'minutos_partida': 15,
        'segundos_partida': 65,
        'horas_duracion': 3,
        'minutos_duracion': 8,
        'segundos_duracion': 9
    }
]

print(calcula_hora_llegada(vuelos))
