channels = [
    'Facebook',
    'Instagram',
    'Feria',
    'WhatsApp'
]
print(channels)
print(len(channels))          # Longitud
print(channels[3])            # acceder a una posicion

channels[1] = 'Volante'       # Modificar listas
print(channels)

channels.append('Valla')      # Agregar item
print(channels)

channels.remove('Feria')      # Remover item
print(channels)