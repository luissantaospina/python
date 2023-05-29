# https://www.nachocabanes.com/retos/propuestos.php

# Crea un programa capaz de calcular la suma de los números que se indicarán en la entrada estándar, 
# separados por espacios, y mostrar los resultados en pantalla. Los números pueden ser negativos, 
# grandes y las líneas pueden contener espacios adicionales, por lo que el programa debe ser robusto.

# (Cuidado: no debe ser "amigable", sino estricto: no debe decir nada como "introduce los datos" 
# ni responder con nada como "la suma es..."; debe tomar cada línea de datos de la entrada estándar, 
# analizarla y mostrar los resultados en la salida estándar).

num = 0
nums = []
sum = 0

while 1:
    num = input()
    if num.isspace() or len(num) < 1:
        break
    else:
        nums.append(num)

for j in nums:
    numList = j.split()
    for k in numList:
        sum = sum + int(k)
        
    print(sum)
    sum = 0
