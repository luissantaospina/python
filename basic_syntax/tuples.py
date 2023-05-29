# las tuplas son inmutables, es decir, no se pueden cambiar
names = ('luis', 'santa')
nombre, apellido = names
print(nombre, apellido)

# mixtas
mix = (2, 'luis', True)
print(mix[0:2])     # primer valor: inicio - segundo valor: fin(sin tomarlo)

# Modificar tuplas, transformando a lista
lista = list(mix)    # Convertir a lista
lista[0] = 9         # Modificar
mix = tuple(lista)   # Convertir a tupla

print(mix)
