# Dados dos vectores v1=(x1,x2,...,xn) y v2=(y1,y2,...,yn), 
# su producto escalar es un número, que se calcula como x1y1+x2y2+...+xnyn.

# Supongamos que puedes permutar las coordenadas de cada vector como desee. 
# Debes escoger dos permutaciones de tal manera que el producto escalar de los dos nuevos vectores 
# sea el menor posible, 
# y mostrar ese producto escalar mínimo.

# La primera línea del archivo de entrada contiene el número de casos de prueba. 
# Para cada caso de prueba, la primera línea contiene n número entero, 
# que es la cantidad de coordenadas de cada vector. Las dos líneas siguientes contienen n enteros cada una, 
# que son las coordenadas de v1 y v2, respectivamente.

# Para cada caso de prueba, la salida será una línea "Case #X: Y", donde X es el número de caso de prueba 
# (contando a partir de 1), e Y es el producto escalar mínimo de todas las permutaciones de los dos vectores dados.

# Límites
# En cuanto a los posibles valores de entrada, en el "conjunto de datos pequeño", 
# habrá 1.000 casos, de no más de 8 coordenadas, con valores entre -1.000 y 1.000; 
# en el "conjunto grande", habrá 10 casos, de entre 100 y 800 coordenadas, con valores entre -100.000 y 100.000;

# Nota: el programa no debe avisar al usuario con mensajes como "Introduzca un número". 
# Debe leer directamente el número que introduzca el usuario y 
# la respuesta debe ser exactamente como se puede comprobar en el ejemplo ("Case #n: ...").

numberTests = int(input())
n = []

for i in range(numberTests):
    rows = int(input())
    for j in range(rows):
        value = int(input())
        n.append(value)
        
print(n)
