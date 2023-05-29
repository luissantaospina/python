# Cuando un rey abdica, su primogénito hereda el trono y debe recibir, en su coronación,
# un número que lo identificará para la posteridad.
# La numeración es importante porque, de otro modo, sería difícil diferenciar a reyes
# con el mismo nombre de una misma dinastía al compartir también apellido.

# El resultado es que ante la abdicación de un rey, toca revisar los libros de historia
# para averiguar su número. ¿Eres capaz de hacerlo tú?

# Entrada
# El programa recibirá, por la entrada estándar, múltiples casos de prueba. 
# Cada uno consta de una primera línea con un número indicando la cantidad de reyes de una determinada dinastía. 
# A continuación vendrá, en otra linea, los nombres de todos sus reyes separados por espacio.

# Después aparecerán dos líneas más, una con la cantidad de sucesores futuros que hay que numerar (al menos uno), 
# y otra con sus nombres separados por espacio.Después aparecerán dos líneas más, 
# una con la cantidad de sucesores futuros que hay que numerar (al menos uno),
# y otra con sus nombres separados por espacio.

# Todos los nombres estarán compuestos de una única palabra de no más de 20 letras del alfabeto inglés,
# y serán sensibles a mayúsculas. Además, se garantiza que en cada caso de prueba no habrá
# más de 20 nombres de reyes diferentes.

# La entrada acaba con un caso de prueba sin potitos.

# Salida
# Para cada sucesor de cada caso de prueba se indicará, una línea independiente, el número que le corresponderá. 
# Aunque normalmente se utilizan números romanos, por simplicidad se indicará
# el número en la notación arábiga tradicional.
# Después de cada caso de prueba se escribirá una línea en blanco.

numberOfPastKings = int(input('Ingrese el numero de reyes pasados: '))
namesOfPastKings = []
for x in range(numberOfPastKings):
    valor = input('Ingrese el nombre del rey pasado n°' + str(x + 1) + ': ')
    namesOfPastKings.append(valor)

numberOfFutureKings = int(input('Ingrese el numero de reyes futuros: '))
namesOfFutureKings = []
for y in range(numberOfFutureKings):
    valor = input('Ingrese el nombre del rey futuro n°' + str(y + 1) + ': ')
    namesOfFutureKings.append(valor)

repeated = {}

for i in namesOfPastKings:
    if i in repeated:
        repeated[i] += 1
    else:
        repeated[i] = 1

for j in namesOfFutureKings:
    if j in repeated:
        print(j, repeated[j] + 1)
        repeated[j] += 1
    else: 
        print(j + ' 1')
        repeated[j] = 1
