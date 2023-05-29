# Retomemos el ejemplo de los diccionarios que representan los estudiantes de la universidad. Cada estudiante tendrá un
# nombre, código, género, carrera, promedio y semestre según créditos. Estas características son las que nos permiten
# definir las claves o llaves que podemos ver en el diccionario de ejemplo. Todos los diccionarios que representen
# estudiantes tendrán la misma estructura, es decir, las mismas claves. Pasemos, ahora sí, a nuestros ejercicios.
# Vamos a crear tres funciones sobre grupos de cuatro estudiantes, cada uno representado por uno de los diccionarios
# que vimos anteriormente. Empecemos con nuestra primera función. Debemos crear una función llamada buscar_estudiante
# que recibe los cuatro diccionarios que representan los estudiantes y un string que corresponde al nombre
# de un estudiante. La función debe retornar el diccionario del estudiante cuyo nombre es idéntico al dado por el
# parámetro o None, en caso de que ninguno de los estudiantes tenga dicho nombre. Se nos solicita asímismo crear
# el programa principal que nos permita ejecutar la función. Pasemos a Spider y veamos la solución. Tenemos nuestra
# función buscar_estudiante, que recibe como parámetro los cuatro diccionarios y el nombre. Vamos a empezar creando
# una variable en la que almacenaremos el diccionario del estudiante buscado, en caso de que exista. Lo llamaremos
# buscado y tendrá el valor None inicialmente, teniendo en cuenta que este es el valor a retornar en caso de que no
# se encuentre un estudiante con el nombre dado por parámetro.


def menu() -> None:
    while 1:
        nivel_actividad_fisica = input('\nQue acción desea realizar: '
                                       '\n1: Ver estudiantes'
                                       '\n2: Crear estudiantes'
                                       '\n3: Buscar estudiante'
                                       '\n4: Avanzar de semestre los estudiantes'
                                       '\n5: Ver estudiantes en riesgo'
                                       '\n')
        match nivel_actividad_fisica:
            case '1':
                print(estudiantes)
            case '2':
                for i in range(4):
                    estudiantes.append(crea_estudiante(i))
            case '3':
                estudiante_a_buscar = input('Ingrese el nombre del estudiante a buscar: ')
                buscar_estudiante(estudiantes, estudiante_a_buscar)
            case '4':
                avanzar_semestre(estudiantes)
                print('Los estudiantes fueron avanzados de semestre con éxito')
            case '5':
                estudiantes_en_riesgo(estudiantes)
            case _:
                print('El valor ingresado no es correcto, por favor rectifica')


def crea_estudiante(iterador: int) -> dict:
    modelo_estudiante['nombre'] = input('Ingrese el nombre del estudiante n°' + str(iterador + 1) + ': ')
    modelo_estudiante['código'] = int(input('Ingrese el código del estudiante n°' + str(iterador + 1) + ': '))
    modelo_estudiante['genero'] = input('Ingrese el genero del estudiante n°' + str(iterador + 1) + ': ')
    modelo_estudiante['carrera'] = input('Ingrese la carrera del estudiante n°' + str(iterador + 1) + ': ')
    modelo_estudiante['promedio'] = float(input('Ingrese el promedio del estudiante n°' + str(iterador + 1) + ': '))
    modelo_estudiante['ssc'] = int(input('Ingrese el ssc del estudiante n°' + str(iterador + 1) + ': '))
    return modelo_estudiante


def buscar_estudiante(estudiantes_a_buscar: list, nombre_estudiante_a_buscar: str) -> None:
    estudiante_encontrado = ''
    for estudiante in estudiantes_a_buscar:
        if estudiante['nombre'] == nombre_estudiante_a_buscar:
            estudiante_encontrado = estudiante

    if estudiante_encontrado:
        print('El estudiantes es', estudiante_encontrado)
    else:
        print('No se encontró el estudiante')


def avanzar_semestre(estudiantes_a_avanzar: list) -> None:
    for estudiante_a_avanzar in estudiantes_a_avanzar:
        estudiante_a_avanzar['ssc'] += 1


def estudiantes_en_riesgo(lista_estudiantes: list) -> None:
    lista_estudiantes_en_riesgo = []
    for estudiante in lista_estudiantes:
        if estudiante['promedio'] < 3.4:
            lista_estudiantes_en_riesgo.append(estudiante)
    if len(lista_estudiantes_en_riesgo) == 0:
        print('No hay estudiantes en riesgo')
    elif len(lista_estudiantes_en_riesgo) == 1:
        print('El estudiante en riesgo es', lista_estudiantes_en_riesgo)
    else:
        print('Los estudiantes en riesgo son', lista_estudiantes_en_riesgo)


modelo_estudiante = {
    'nombre': '',
    'código': 0,
    'genero': '',
    'carrera': '',
    'promedio': 0.0,
    'ssc': 0
}
estudiantes = []

# Array de estudiantes de ejemplo
# estudiantes = [
#     {
#         'nombre': 'luis',
#         'código': 1234,
#         'genero': 'masculino',
#         'carrera': 'software',
#         'promedio': 4.8,
#         'ssc': 1
#     },
#     {
#         'nombre': 'daniela',
#         'código': 2345,
#         'genero': 'femenino',
#         'carrera': 'derecho',
#         'promedio': 5.0,
#         'ssc': 2
#     },
#     {
#         'nombre': 'carlos',
#         'código': 3456,
#         'genero': 'masculino',
#         'carrera': 'diseño',
#         'promedio': 4.0,
#         'ssc': 3
#     },
#     {
#         'nombre': 'andrea',
#         'código': 4567,
#         'genero': 'femenino',
#         'carrera': 'artes',
#         'promedio': 3.3,
#         'ssc': 4
#     }
# ]

menu()
