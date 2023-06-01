channels = [
    'Facebook',
    'Instagram',
    'Feria',
    'WhatsApp'
]

channels_two = [
    'Facebook',
    'Instagram',
    'Feria',
    'WhatsApp'
]

print(channels)
print(len(channels))  # Longitud
print(channels[2])  # acceder a una posición
print(channels[-1])  # acceder a la última posición

# Modificar listas
channels[1] = 'Volante'
print(channels)

# Agregar item
channels.append('Valla')
print(channels)

# Agregar item en un index especifico
channels.insert(0, 'Pasacalle')
print(channels)

# Remover item
channels.remove('Feria')
print(channels)

# Remover item con un index especifico
del channels[1]
print(channels)

# Remover ultimo elemento
channels.pop()
print(channels)

# Unir dos listas
channels.extend(channels_two)
print(channels)

# Ver indice
print(channels.index('Instagram'))

# Remover todos los elementos
channels.clear()
print(channels)
