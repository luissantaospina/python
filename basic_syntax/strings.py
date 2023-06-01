name = 'luis'
last_name = '''luis 
    fernando'''

name_whit_age = 'luis {}'
age = 27

for i in name:
    print(i)

print(len(name))  # longitud
print(last_name)  # imprimir con salto
print(name * 3)  # imprimir en 3 veces
print(name[3])  # acceder a una posición
print(name.upper())  # mayúscula
print(name.lower())  # minúscula
print(name.replace('u', 'o'))  # reemplaza una letra
print(name_whit_age.format(age))  # Dar formato a variable
