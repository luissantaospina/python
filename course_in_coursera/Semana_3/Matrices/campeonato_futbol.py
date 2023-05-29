# 1. La primera función debe calcular el total de goles marcados en el campeonato. Esto es, básicamente,
# calcular la suma de todos los goles que están en la matriz que contiene la tabla de goles, lo cual
# podemos lograr con un recorrido total, usando dos ciclos sobre la matriz
# 2. La segunda función debe calcular el total de partidos que se han jugado hasta el momento. Para esto,
# debemos buscar dentro del tablero de goles, los resultados que sean diferentes a menos uno y menos dos,
# pero teniendo en cuenta que no debemos contar dos veces un mismo partido, por lo que un resultado está
# dado por los goles de cada uno de los equipos
# 3. Ahora queremos conocer el equipo que más goles ha marcado en el torneo. Para conocer los goles de un
# equipo, debemos recorrer la fila que le corresponda


def lee_equipos() -> dict:
    lista_equipos = {}
    archivo = open('equipos_futbol.txt')
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(';')
        lista_equipos[datos[0]] = int(datos[1])
        linea = archivo.readline()
    archivo.close()
    return lista_equipos


def suma_goles(tabla_goles: list) -> int:
    sumatoria_goles = 0
    for i in range(len(tabla_goles)):
        for j in range(len(tabla_goles[i])):
            if tabla_goles[i][j] >= 0:
                sumatoria_goles += tabla_goles[i][j]
    return sumatoria_goles


def suma_partidos(tabla_goles: list) -> int:
    sumatoria_partidos = 0
    for i in range(len(tabla_goles)):
        for j in range(len(tabla_goles[i])):
            if tabla_goles[i][j] >= 0:
                sumatoria_partidos += 1
    return sumatoria_partidos // 2


def equipo_goleador(tabla_goles: list, lista_equipos: dict) -> str:
    sumatoria_fila = 0
    mas_goles = 0
    fila_mas_goles = 0
    for i in range(len(tabla_goles)):
        for j in range(len(tabla_goles[i])):
            if tabla_goles[i][j] >= 0:
                sumatoria_fila += tabla_goles[i][j]
        if sumatoria_fila > mas_goles:
            mas_goles = sumatoria_fila
            fila_mas_goles = i
        sumatoria_fila = 0
    equipo_mas_goles = list(lista_equipos.keys())[list(lista_equipos.values()).index(fila_mas_goles)]
    return equipo_mas_goles


goles = [
    [-1, 1, 1, 1, 1, 1, 1, 1],
    [1, -1, 1, 1, 1, 1, 1, 1],
    [1, 1, -1, 1, -2, 1, 8, 1],
    [1, 1, 1, -1, 1, -2, 1, -2],
    [1, 1, -2, 1, -1, 1, 1, 1],
    [1, 3, 1, -2, 1, -1, 1, 1],
    [1, 1, 1, 1, 1, 1, -1, -2],
    [1, 4, 1, -2, 1, 1, -2, -1]
]
equipos = lee_equipos()
print(equipos)

print('La sumatoria de los goles es', suma_goles(goles))
print('La sumatoria de todos los partidos es', suma_partidos(goles))
print('El equipo mas goleador es el', equipo_goleador(goles, equipos))
