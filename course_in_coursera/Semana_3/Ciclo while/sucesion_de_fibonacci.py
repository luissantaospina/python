# En matemáticas, la sucesión o serie de Fibonacci es la siguiente sucesión infinita de números
# naturales: 0,1,1,2,3,5,8,13,...
#
#  La sucesión comienza con los números 0 y 1, y a partir de estos, cada término es la suma de los dos anteriores.
#
# Cree una función que reciba un número que indica la cantidad de números de la sucesión que se quieren
# encontrar y retorne una cadena con los números separados por coma.
#
# Por ejemplo, el resultado de la función, si se pasa como parámetro el número 18 es el siguiente:
#
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: sucesion_fibonacci
#
# Si lo requiere, puede agregar funciones adicionales.


def sucesion_fibonacci(cantidad_numeros_secesion: int) -> str:
    a, b = 0, 1
    sucesion = ''
    iterador = 0
    while iterador < cantidad_numeros_secesion:
        sucesion += str(a) + ','
        a, b = b, a + b
        iterador += 1
    return sucesion[:-1]


def sucesion_fibonacci_con_for(cantidad_numeros_secesion: int) -> str:
    a, b = 0, 1
    sucesion = ''
    for _ in range(cantidad_numeros_secesion):
        sucesion += str(a) + ','
        a, b = b, a + b
    return sucesion[:-1]


cantidad_digitos_sucesion = int(input('Ingrese la cantidad de dígitos a encontrar en la sucesión fibonacci: '))
print(sucesion_fibonacci(cantidad_digitos_sucesion))
