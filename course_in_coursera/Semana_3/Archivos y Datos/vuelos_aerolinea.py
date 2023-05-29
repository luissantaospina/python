# Primero, vamos a escribir una función que nos permita conocer
# los códigos de todos los vuelos que parten de un determinado aeropuerto.
# Nuestra función recibirá como parámetro el diccionario de vuelos y el código
# de un aeropuerto, y retornará a una lista con los códigos de los vuelos.


# La segunda función que implementaremos nos permite conocer el código del vuelo
# más largo, es decir, el de mayor duración de una aerolínea. Para este caso, necesitamos
# que la función reciba por parámetro el diccionario de vuelos y el código de una de las aerolíneas


# En este se nos pide implementar una función que permita conocer el código del aeropuerto más visitado,
# teniendo en cuenta tanto los vuelos que salen de éste, como los que llegan.


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
        vuelo['distancia'] = datos[4]
        vuelo['salida'] = datos[5]
        vuelo['duracion'] = datos[6]
        vuelo['retraso'] = datos[7]
        vuelos[codigo_vuelo] = vuelo
        linea = archivo.readline()
    archivo.close()
    return vuelos


def vuelos_por_aeropuerto(lista_vuelos: dict, codigo_aeropuerto: str) -> list:
    vuelos_aeropuerto = []
    for key, value in lista_vuelos.items():
        if value['origen'] == codigo_aeropuerto:
            vuelos_aeropuerto.append(key)
    return vuelos_aeropuerto


def vuelos_mas_largo_por_aerolinea(lista_vuelos: dict, codigo_aerolinea: str) -> str:
    vuelo_mas_largo = ''
    for key, value in lista_vuelos.items():
        if value['aerolinea'] == codigo_aerolinea:
            vuelo_mas_largo = key
    return vuelo_mas_largo


def aeropuerto_mas_visitado(lista_vuelos: dict) -> str:
    vuelos_visitas = {}
    for vuelo in lista_vuelos.values():
        origen = vuelo['origen']
        destino = vuelo['destino']
        vuelos_visitas[origen] = vuelos_visitas.get(origen, 0) + 1
        vuelos_visitas[destino] = vuelos_visitas.get(destino, 0) + 1

    mas_visitas = max(vuelos_visitas.values())
    aeropuerto_mas_visitas = list(vuelos_visitas.keys())[list(vuelos_visitas.values()).index(mas_visitas)]
    return aeropuerto_mas_visitas


aeropuerto_a_buscar_vuelos = 'YUU'
print('Los vuelos con origen del aeropuerto', aeropuerto_a_buscar_vuelos, 'son:',
      vuelos_por_aeropuerto(lee_vuelos(), aeropuerto_a_buscar_vuelos))

aerolinea_a_buscar_vuelo_largo = 'QWE'
print('El vuelo mas largo de la aerolínea', aerolinea_a_buscar_vuelo_largo, 'es:',
      vuelos_mas_largo_por_aerolinea(lee_vuelos(), aerolinea_a_buscar_vuelo_largo))

print('El aeropuerto mas visitado es:', aeropuerto_mas_visitado(lee_vuelos()))
