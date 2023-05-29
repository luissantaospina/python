# Nicolás es un novio muy amoroso, pero tiene fama de ser tacaño. Para el cumpleaños
# de su novia ha pedido un catálogo de artículos para escoger el regalo más barato
# disponible. El catálogo es un diccionario que tiene varias llaves que corresponden
# al nombre de los productos. El valor asociado a cada llave es el precio del producto.
#
# Cree una función que retorne el nombre del artículo más barato en el catálogo.
#
# Si Nicolás encuentra dos artículos igual de baratos, comprará el que tenga el nombre
# alfabéticamente menor (el que aparecería antes en el diccionario ignorando las mayúsculas y minúsculas).
#
# Si el artículo más barato vale más de 10.000 pesos, Nicolás no comprará nada e invitará
# a su novia a ver una película en su casa.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: producto_mas_barato
# Si lo requiere, puede agregar funciones adicionales.
#
# El nombre del artículo más barato en el catálogo. Si no hay ningún artículo que valga menos de
# 10.000, retornará None. Si el catálogo está vacío, retornará la cadena "No hay productos para escoger".


def producto_mas_barato(catalogo: dict) -> str:
    if not catalogo:
        producto_barato = 'No hay productos para escoger'
    else:
        catalogo_ordenado = dict(sorted(catalogo.items()))
        precio_producto_barato = min(catalogo_ordenado.values())
        producto_barato = list(catalogo_ordenado.keys())[list(catalogo_ordenado.values()).index(precio_producto_barato)]
        if precio_producto_barato > 10000:
            producto_barato = None
    return producto_barato


lista_productos = {
    'locion': 120000,
    'blusa': 50000,
    'jean': 70000,
    'crema': 25000,
    'chocolates': 5000,
    'galletas': 55500,
    'bombones': 5000,
}

print(producto_mas_barato(lista_productos))
