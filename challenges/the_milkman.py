# Usted es empresario en Madrid, y tiene la brillante idea de abrir una tienda de la leche en la Plaza Mayor. 
# Como es una persona muy prudente, desea que la leche que venderá sea perfectamente natural y fresca, y por esa razón, 
# va a traer unas sanísimas vacas de la región de Zaragoza a Madrid. Tiene a su disposición un camión con un cierto límite de peso, 
# y un grupo de vacas disponibles para la venta. Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.

# Su objetivo como empresario es elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de leche, observando el límite de peso del camión.

# Entrada: Número total de vacas en la zona de Zaragoza que están a la venta.
# Entrada: Peso total que el camión puede llevar.
# Entrada: Lista de pesos de las vacas.
# Entrada: Lista de la producción de leche por vaca, en litros por día.
# Salida: Cantidad máxima de producción de leche se puede obtener.



cows = 6
truckWeightLimit = 700
weightCows = [360, 250, 400, 180, 50, 90]
milkPerCow = [40, 35, 43, 28, 12, 13]

class cow:
    def __init__(self, id, weight, milk):
        self.id = id
        self.weight = weight
        self.milk = milk

cow1 = cow(1, 360, 40)
print(cow1)