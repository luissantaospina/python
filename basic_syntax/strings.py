name = 'luis'
lastName = '''luis 
    fernando'''

nameWhitAge = 'luis {}'
age = 27

for i in name:
    print(i)

print(len(name))                # longitud
print(lastName)                 # imprimir con salto
print(name * 3)                 # imprimir en 3 veces
print(name[3])                  # acceder a una posicion
print(name.upper())             # mayuscula
print(name.lower())             # minuscula
print(name.replace('u', 'o'))   # reemplaza una letra
print(nameWhitAge.format(age))  # Dar formato a variable