"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Luis Santa
"""


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """
    pelicula = {
        'nombre': nombre,
        'genero': genero,
        'duracion': duracion,
        'anio': anio,
        'clasificacion': clasificacion,
        'hora': hora,
        'dia': dia
    }
    return pelicula


def encontrar_pelicula(nombre_pelicula_a_buscar: str, peliculas: list) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula_a_buscar (str): El nombre de la pelicula que se desea encontrar.
        peliculas (list) = lista de peliculas
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    pelicula_encontrada = None
    for pelicula in peliculas:
        if pelicula['nombre'] == nombre_pelicula_a_buscar:
            pelicula_encontrada = pelicula
    return pelicula_encontrada


def encontrar_pelicula_mas_larga(peliculas: list) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        peliculas (list) = lista de peliculas
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    mayor_duracion = 0
    pelicula_mas_larga = {}
    for pelicula in peliculas:
        if pelicula['duracion'] > mayor_duracion:
            pelicula_mas_larga = pelicula
            mayor_duracion = pelicula['duracion']
    return pelicula_mas_larga


def duracion_promedio_peliculas(peliculas: list) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        peliculas (list) = lista de peliculas
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    duracion_peliculas = 0
    for pelicula in peliculas:
        duracion_peliculas += pelicula['duracion']
    promedio = int(duracion_peliculas / 5)
    horas, minutos = divmod(promedio, 60)
    return str(horas) + ':' + str(minutos)


def encontrar_estrenos(peliculas: list, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        peliculas (list) = lista de peliculas
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    estrenos = ''
    for pelicula in peliculas:
        if pelicula['anio'] > anio:
            if estrenos:
                estrenos += ', ' + pelicula['nombre']
            else:
                estrenos += pelicula['nombre']
    if not estrenos:
        estrenos = 'Ninguna'
    return estrenos


def cuantas_peliculas_18_mas(peliculas: list) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        peliculas (list) = lista de peliculas
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    numero_peliculas_mas_18 = 0
    for pelicula in peliculas:
        if pelicula['clasificacion'] == '18+' or pelicula['clasificacion'] == 'Todos':
            numero_peliculas_mas_18 += 1
    return numero_peliculas_mas_18


def reagendar_pelicula(pelicula: dict, nueva_hora: int, nuevo_dia: str,
                       control_horario: bool) -> bool:
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    if not control_horario:
        puede_reagendar = True
    else:
        if pelicula['genero'].find('Documental') >= 0 and nueva_hora > 2200:
            puede_reagendar = False
        elif pelicula['genero'].find('Drama') >= 0 and nuevo_dia == 'Viernes':
            puede_reagendar = False
        elif nuevo_dia != 'Sabado' and nuevo_dia != 'Domingo' and nueva_hora <= 600 or nueva_hora >= 2100:
            puede_reagendar = False
        else:
            puede_reagendar = True

    if puede_reagendar:
        pelicula['hora'] = nueva_hora
        pelicula['dia'] = nuevo_dia
    return puede_reagendar


def decidir_invitar(pelicula: dict, edad_invitado: int, autorizacion_padres: bool = False) -> bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        pelicula (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    se_puede_invitar = False
    if edad_invitado >= 18:
        se_puede_invitar = True
    if edad_invitado <= 10 and pelicula['clasificacion'].find('Familiar') >= 0:
        se_puede_invitar = True
    if pelicula['genero'].find('Documental') >= 0:
        se_puede_invitar = True
    if edad_invitado < 18 and pelicula['genero'].find('Documental') < 0 and autorizacion_padres:
        se_puede_invitar = True
    return se_puede_invitar


def pedir_autorizacion() -> bool:
    valor_autorizacion = False
    fin_ciclo = False
    while not fin_ciclo:
        autorizacion = input('El menor de edad cuenta con autorización de los padres\n1: Si\n2: No\n')
        if autorizacion == '1':
            valor_autorizacion = True
            fin_ciclo = True
        elif autorizacion == '2':
            fin_ciclo = True
        else:
            print('La opción', autorizacion, 'no es valida')
    return valor_autorizacion


def pedir_preferencias() -> bool:
    valor_preferencias = False
    fin_ciclo = False
    while not fin_ciclo:
        preferencia = input('Desea tener en cuenta sus preferencias\n1: Si\n2: No\n')
        if preferencia == '1':
            valor_preferencias = True
            fin_ciclo = True
        elif preferencia == '2':
            fin_ciclo = True
        else:
            print('La opción', preferencia, 'no es valida')
    return valor_preferencias
