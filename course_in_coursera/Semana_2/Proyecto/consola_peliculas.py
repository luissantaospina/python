"""
Ejercicio nivel 2: Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
"""
import modulo_peliculas as mod


def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """       
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins")
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if hora // 100 < 10:
        hora_formato = "0" + str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if hora % 100 < 10:
        min_formato = "0" + str(hora % 100)
    else:
        min_formato = str(hora % 100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)


def ejecutar_encontrar_pelicula(peliculas: list) -> None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        peliculas (list) = lista de peliculas
    """
    nombre = input('Ingrese el nombre de la película a buscar: ')
    pelicula = mod.encontrar_pelicula(nombre, peliculas)
    if pelicula is None:
        print("No hay ninguna película con este nombre")
    else:
        print(pelicula)


def ejecutar_encontrar_pelicula_mas_larga(peliculas: list) -> None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        peliculas (list) = lista de peliculas
    """
    print(mod.encontrar_pelicula_mas_larga(peliculas))


def ejecutar_consultar_duracion_promedio_peliculas(peliculas: list) -> None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas.
    Parametros:
        peliculas (list) = lista de peliculas
    """
    print(mod.duracion_promedio_peliculas(peliculas))


def ejecutar_encontrar_estrenos(peliculas: list) -> None:
    """ Ejecuta la opcion de buscar peliculas de estreno. Esto es: las peliculas que sean 
        mas recientes que un anio dado.
    Parametros:
        peliculas (list) = lista de peliculas
    """
    anio_consulta = int(input('Ingrese el año a consultar estrenos: '))
    print(mod.encontrar_estrenos(peliculas, anio_consulta))


def ejecutar_cuantas_peliculas_18_mas(peliculas: list) -> None:
    """Ejecuta la opcion de consultar cuantas peliculas de la agenda tienen clasificacion
    18+.
    Parametros:
        peliculas (list) = lista de peliculas
    """
    print(mod.cuantas_peliculas_18_mas(peliculas))


def ejecutar_reagendar_pelicula(peliculas: list) -> None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        peliculas (list) = lista de peliculas
    """
    nombre_pelicula = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre_pelicula, peliculas)
    
    if pelicula is None:
        print("No hay ninguna película con este nombre")
    else:
        preferencia = mod.pedir_preferencias()
        nueva_hora = int(input('Ingrese la nueva hora en formato 24 horas para la película '
                               + pelicula['nombre'] + ': '))
        nuevo_dia = input('Ingrese el nuevo día para la película ' + pelicula['nombre'] + ': ')
        print(mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, preferencia))


def ejecutar_decidir_invitar(peliculas: list) -> None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        peliculas (list) = lista de peliculas
    """
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    pelicula = mod.encontrar_pelicula(nombre_pelicula, peliculas)
    autorizacion = False

    if pelicula is None:
        print("No hay ninguna película con este nombre")
    else:
        edad = int(input("Ingrese la edad del invitado en años: "))
        if edad < 18 and pelicula['genero'].find('Documental') < 0:
            autorizacion = mod.pedir_autorizacion()

        puede_invitar = mod.decidir_invitar(pelicula, edad, autorizacion)
        if puede_invitar:
            print('La persona SI puede ser invitado para la película', pelicula['nombre'])
        else:
            print('La persona NO puede ser invitado para la película', pelicula['nombre'])


def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    peliculas = []

    peliculas.append(mod.crear_pelicula("Shrek", "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes"))
    peliculas.append(mod.crear_pelicula("Get Out", "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado"))
    peliculas.append(mod.crear_pelicula("Icarus", "Documental, Suspenso", 122, 2019, '18+', 800, "Domingo"))
    peliculas.append(mod.crear_pelicula("Inception", "Acción, Drama", 148, 2010, '13+', 1300, "Lunes"))
    peliculas.append(mod.crear_pelicula("The Empire Strikes Back",
                                        "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles"))
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de películas para la semana de receso" + "\n" + ("-"*50))
        i = 1
        for pelicula in peliculas:
            print('Película', i)
            mostrar_informacion_pelicula(pelicula)
            print("-" * 50)
            i += 1
        
        ejecutando = mostrar_menu_aplicacion(peliculas)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(peliculas: list) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        peliculas (list) = lista de peliculas
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Encontrar película por nombre")
    print(" 2 - Consultar película mas larga")
    print(" 3 - Consultar duración promedio de las películas")
    print(" 4 - Consultar películas de estreno")
    print(" 5 - Consultar cuantas películas tienen clasificación 18+")
    print(" 6 - Reagendar película")
    print(" 7 - Verificar si se puede invitar a alguien")
    print(" 8 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    match opcion_elegida:
        case '1': ejecutar_encontrar_pelicula(peliculas)
        case '2': ejecutar_encontrar_pelicula_mas_larga(peliculas)
        case '3': ejecutar_consultar_duracion_promedio_peliculas(peliculas)
        case '4': ejecutar_encontrar_estrenos(peliculas)
        case '5': ejecutar_cuantas_peliculas_18_mas(peliculas)
        case '6': ejecutar_reagendar_pelicula(peliculas)
        case '7': ejecutar_decidir_invitar(peliculas)
        case '8': continuar_ejecutando = False
        case _: print("La opción " + opcion_elegida + " no es valida.")
    
    return continuar_ejecutando


iniciar_aplicacion()
