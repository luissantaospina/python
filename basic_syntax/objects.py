client = {
    'name': 'Luis',
    'age': 27,
    'phone': 3103830717,
    'email': 'l.santa@gmail.com'
}
print(client)
print(len(client))                      # Longitud
print(client['email'])                  # acceder a un atributo
print(client.keys())                    # acceder a las llaves
print(client.values())                  # acceder a los valores
print(client.items())                   # convertir en listas
client.update({'name': 'Fernando'})     # Actualizar valores
print(client)
del client['age']                       # Elimina item
print(client)