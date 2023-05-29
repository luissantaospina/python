# Recopilamos los registros de los vuelos que ocurrieron durante un día entre aeropuertos ubicados en
# Estados Unidos y los organizamos en un diccionario de diccionarios. Ahora queremos que usted nos
# ayude a averiguar cuál es la mejor aerolínea con base en la puntualidad. Es decir, queremos saber
# cuál es la aerolínea que acumuló el menor retraso promedio en los vuelos que recopilamos.
#
# El parámetro vuelos de la función, es un diccionario de diccionarios con la información de los vuelos.
# Las llaves en este diccionario son el código de cada vuelo.
#
# Los valores en este diccionario son diccionarios con la información de un vuelo organizado de acuerdo
# con las siguientes llaves:
#
# aerolinea, corresponde al nombre de la aerolínea.
# origen, corresponde al código de aeropuerto de origen.
# destino, corresponde al código de aeropuerto destino del vuelo.
# distancia, corresponde a la distancia entre el origen y el destino.
# retraso, corresponde a la cantidad de minutos de retraso que tuvo el vuelo.
# duracion, corresponde a la duración planeada del vuelo en minutos.
# salida, corresponde a un entero que representa la hora de salida.
#
# La hora de salida, se representa usando la hora en formato 24 horas multiplicada por 100 más la
# cantidad de minutos (por ejemplo, las 2007 indica que el vuelo salió a las 8:07 pm).
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
# Nombre de la función: mejor_aerolinea
# Si lo requiere, puede agregar funciones adicionales.


def lee_vuelos() -> dict:
    vuelos = {}
    archivo = open('vuelos.txt')
    linea = archivo.readline()    # Omito los titulos
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(';')
        codigo_vuelo = datos[1]
        vuelo = {}
        vuelo['aerolinea'] = datos[0]
        vuelo['origen'] = datos[2]
        vuelo['destino'] = datos[3]
        vuelo['distancia'] = int(datos[4])
        vuelo['retraso'] = int(datos[7])
        vuelo['duracion'] = int(datos[6])
        vuelo['salida'] = int(datos[5])
        vuelos[codigo_vuelo] = vuelo
        linea = archivo.readline()
    archivo.close()
    return vuelos


def mejor_aerolinea(lista_vuelos: dict) -> str:
    aerolinea_retraso = {}
    for vuelo in lista_vuelos.values():
        if not aerolinea_retraso.get(vuelo['aerolinea']):
            aerolinea_retraso[vuelo['aerolinea']] = [vuelo['retraso'], 1]
        else:
            aerolinea_retraso[vuelo['aerolinea']] = [aerolinea_retraso[vuelo['aerolinea']][0] + vuelo['retraso'],
                                                     aerolinea_retraso[vuelo['aerolinea']][1] + 1]

    for key, value in aerolinea_retraso.items():
        aerolinea_retraso[key] = value[0] / value[1]

    mas_visitas = min(aerolinea_retraso.values())
    aeropuerto_mas_visitas = list(aerolinea_retraso.keys())[list(aerolinea_retraso.values()).index(mas_visitas)]
    return aeropuerto_mas_visitas


print(mejor_aerolinea(lee_vuelos()))
