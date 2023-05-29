# Una agencia de viajes necesita informar a sus clientes la hora de llegada de sus vuelos.
# Se conoce la hora de partida del vuelo (en horas, minutos y segundos) y la duración del vuelo
# (en horas, minutos y segundos).
#
# Cree una función que retorne la hora de llegada del vuelo en una cadena con el formato
# “HH:mm:ss” donde HH es la hora, mm los minutos y ss los segundos de la hora de llegada del vuelo.
#
# La hora está dada en formato de 24 horas. Si alguno de los 3 números de la respuesta
# es menor a 10, solo se necesita un dígito ('7' en lugar de '07').
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: calcular_horario_llegada
#
# Si lo requiere, puede agregar funciones adicionales.
import datetime


def check_out(hh_check: int, mm_check: int, ss_check: int, hh_flight, mm_flight, ss_flight) -> str:
    d2 = datetime.timedelta(hours=hh_check, minutes=mm_check, seconds=ss_check)
    d3 = datetime.timedelta(hours=hh_flight, minutes=mm_flight, seconds=ss_flight)
    return str(d2 + d3)


hh_check_in = 10
mm_check_in = 30
ss_check_in = 60
hh_flight_duration = 15
mm_flight_duration = 25
ss_flight_duration = 1

print(check_out(hh_check_in, mm_check_in, ss_check_in, hh_flight_duration, mm_flight_duration, ss_flight_duration))
