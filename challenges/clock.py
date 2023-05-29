# Tienes un reloj digital con LEDs de 7 segmentos. Un día, al despertar de un sueño de ciencia-ficción,
# te preguntas: ¿cuántos segmentos se han encendido DESPUÉS DE X segundos, desde la posición 00:00:00?

# Considera que en cada segundo, todos los led se apagan y luego se encienden los correspondientes al instante actual.

# (Recuerda: no debe ser "amigable", sino estricto: no debe decir nada como "introduce los segundos" ni
# responder con nada como "la cantidad de LEDs es...";
# debe tomar cada línea de datos de la entrada estándar, analizarla y mostrar los resultados en la salida
# estándar, tantas veces como líneas de entrada existan).

seconds = input()
lineForNumber = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 5
}

sumThanLines = 0

for i in seconds:
    for j in range(int(i) + 1):
        sumThanLines = sumThanLines + lineForNumber[j]

print(sumThanLines)
