# punto 1
x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x += 5
    elif a > 5:
        x += 4
    else:
        x += 3
else:
    x += 2
print(x)

# punto 2
banco = {
    'nombre': 'Techo',
    'localidad': 'Kennedy',
    'donantes': 0,
    'AB+': 360,
    'AB-': 130
}

llave1 = 'localidad'
llave2 = 'Kennedy'

valor1 = banco.get(llave1, 'ninguno')
valor2 = banco.get(llave2, 'ninguno')

print(valor1)
print(valor2)

banco['nombre'] = 'Banderas'
print(valor1)

#punto 3
banco = {
    'nombre': 'Shaio',
    'localidad': 'Suba',
    'donantes': 1023,
    'sangre_o+': 100,
    'sangre_o-': 200
}

temporal1 = 0
if banco['sangre_o+'] > 120:
    temporal1 = 3
if banco['sangre_o-'] > 50:
    temporal1 = 7

print(temporal1)

if banco['localidad'].lower() == 'shaio':
    temporal1 = 5
if banco['sangre_o+'] <= 700:
    temporal1 = 15
if banco['localidad'] != 'Suba':
    temporal1 = 30
else:
    temporal1 = 20

print(temporal1)

#punto 4
banco = {
    'nombre': 'Bachue',
    'localidad': 'Engativa',
    'donantes': 367,
    'sangre_A+': 856,
    'sangre_A-': 348
}

banco['localidad'] = 'Banderas'
temporal1 = 0

if banco['localidad'].lower() == 'engativa':
    temporal1 = 5
elif banco['sangre_A+'] > 700:
    temporal1 = 15
elif banco['localidad'] != 'Suba':
    temporal1 = 30
else:
    temporal1 = 20

print(temporal1)
