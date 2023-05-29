# Catalina necesita llevar un mejor control de sus gastos cuando hace mercado. Para esto,
# ha decidido construir una aplicación para registrar cada producto que agregue en su carrito
# de compras. Estos datos son guardados en un diccionario cuyas llaves corresponden a los
# nombres de los productos. El valor asociado a cada llave es el precio del producto correspondiente.
#
# Cree una función que retorne el valor total del carrito de compras. Esto es, la suma de
# los precios individuales de todos los productos que están en el carrito.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: valor_carrito_compras
# Si lo requiere, puede agregar funciones adicionales


def valor_carrito_compras(lista_productos: dict) -> float:
    valor_total = 0
    for producto in lista_productos.values():
        valor_total += producto
    return valor_total


carrito_productos = {
    'leche': 4100,
    'arepas': 2500,
    'huevos': 16200,
    'pan': 3000,
    'cafe': 6500
}

print(valor_carrito_compras(carrito_productos))
