# Conditionals
price = int(input()) # Validate type

if price > 100:
    print('Es mayor a 100')
elif price == 0:
    print('Es cero')
else:
    print('Es menor a 100')


# Swith case
def http_error(status):
    match status:
        case 400:
            return "Solicitud incorrecta"
        case 404:
            return "No encontrado"
        case 500:
            return "Error en el servidor"
        case _:  #defaul
            return "Algo anda mal en internet"
print(http_error(400))