def cargar_canciones(archivo_a_cargar: str) -> list:
    canciones = []
    try:
        archivo = open(archivo_a_cargar)
        linea = archivo.readline()
        linea = archivo.readline()
        while len(linea) > 0:
            datos = linea.split(',')
            cancion = {}
            cancion['posicion'] = int(datos[0])
            cancion['nombre_cancion'] = datos[1]
            cancion['nombre_artista'] = datos[2]
            cancion['anio'] = int(datos[3])
            cancion['letra'] = datos[4]
            canciones.append(cancion)
            linea = archivo.readline()
        archivo.close()
    except FileNotFoundError:
        canciones = []
    return canciones


def buscar_cancion(lista_canciones: list, cancion_buscar: str, anio_buscar: int) -> dict:
    cancion_encontrada = None
    for cancion in lista_canciones:
        if cancion['nombre_cancion'] == cancion_buscar and cancion['anio'] == anio_buscar:
            cancion_encontrada = cancion
    return cancion_encontrada


def buscar_canciones_anio(lista_canciones: list, anio_buscar: int) -> list:
    canciones_encontradas = []
    for cancion in lista_canciones:
        if cancion['anio'] == anio_buscar:
            cancion.pop('letra', None)
            canciones_encontradas.append(cancion)
    return canciones_encontradas


def buscar_canciones_artista_periodo(lista_canciones: list,
                                     artista_buscar: str,
                                     anio_ini_buscar: int,
                                     anio_fin_buscar: int) -> list:
    canciones_encontradas = []
    for cancion in lista_canciones:
        if anio_ini_buscar <= cancion['anio'] <= anio_fin_buscar and cancion['nombre_artista'] == artista_buscar:
            cancion.pop('letra', None)
            canciones_encontradas.append(cancion)
    return canciones_encontradas


def buscar_canciones_artista(lista_canciones: list, artista_buscar: str) -> list:
    canciones_encontradas = []
    for cancion in lista_canciones:
        if cancion['nombre_artista'] == artista_buscar:
            cancion.pop('letra', None)
            canciones_encontradas.append(cancion)
    return canciones_encontradas


def buscar_todos_artistas_cancion(lista_canciones: list, cancion_buscar: str) -> list:
    artistas_encontrados = []
    for cancion in lista_canciones:
        if cancion['nombre_cancion'] == cancion_buscar:
            artistas_encontrados.append(cancion['nombre_artista'])
    return artistas_encontrados


def buscar_artistas_mas_populares(lista_canciones: list, min_canciones: int) -> dict:
    artistas_canciones = {}
    artistas_encontrados = {}
    for cancion in lista_canciones:
        if not artistas_canciones.get(cancion['nombre_artista']):
            artistas_canciones[cancion['nombre_artista']] = 1
        else:
            artistas_canciones[cancion['nombre_artista']] += 1
    for key, value in artistas_canciones.items():
        if value > min_canciones:
            artistas_encontrados[key] = value
    return artistas_encontrados


def buscar_artista_estrella(lista_canciones: list) -> dict:
    artistas_canciones = {}
    artista_estrella = {}
    for cancion in lista_canciones:
        if not artistas_canciones.get(cancion['nombre_artista']):
            artistas_canciones[cancion['nombre_artista']] = 1
        else:
            artistas_canciones[cancion['nombre_artista']] += 1
    mas_canciones = max(artistas_canciones.values())
    artista = list(artistas_canciones.keys())[list(artistas_canciones.values()).index(mas_canciones)]
    artista_estrella[artista] = mas_canciones
    return artista_estrella


def buscar_artistas_y_sus_canciones(lista_canciones: list) -> dict:
    artistas_canciones = {}
    for cancion in lista_canciones:
        if not artistas_canciones.get(cancion['nombre_artista']):
            artistas_canciones[cancion['nombre_artista']] = [cancion['nombre_cancion']]
        elif cancion['nombre_cancion'] not in artistas_canciones[cancion['nombre_artista']]:
            artistas_canciones[cancion['nombre_artista']] += [cancion['nombre_cancion']]
    return artistas_canciones


def calcula_promedio_canciones_por_artista(lista_canciones: list) -> int:
    canciones_diferentes = []
    artistas_diferentes = []
    for cancion in lista_canciones:
        if cancion['nombre_cancion'] not in canciones_diferentes:
            canciones_diferentes.append(cancion['nombre_cancion'])
        if cancion['nombre_artista'] not in artistas_diferentes:
            artistas_diferentes.append(cancion['nombre_artista'])
    canciones_promedio_artista = len(canciones_diferentes) // len(artistas_diferentes)
    return canciones_promedio_artista
