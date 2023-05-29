# El área de un triángulo puede ser calculada cuando se conoce la longitud de sus lados.
# Teniendo en cuenta que s1, s2 y s3 son las longitudes de los lados del triángulo, se puede calcular el sub perímetro
# s = (s1+s2+s3)/2, y, con este valor, se puede calcular el área del triángulo de la siguiente manera:
# area = √( s * (s-s1) * (s-s2) * (s-s3) ).
#
# Cree una función que recibe la medida de los lados del triángulo y retorna el área de este,
# redondeada a una cifra decimal.
#
# El módulo math puede serle de ayuda para calcular la raíz cuadrada.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: area_triangulo

import math


def triangle_area(sub_perimeter_1: float, sub_perimeter_2: float, sub_perimeter_3: float) -> object:
    """
    :rtype: float
    """
    total_sub_perimeter = (sub_perimeter_1 + sub_perimeter_2 + sub_perimeter_3) / 2
    area = round(math.sqrt(total_sub_perimeter * (total_sub_perimeter - sub_perimeter_1) *
                           (total_sub_perimeter - sub_perimeter_2) *
                           (total_sub_perimeter - sub_perimeter_3)), 1)
    return area


s1 = float(input('Ingrese la longitud del lado n°1: '))
s2 = float(input('Ingrese la longitud del lado n°2: '))
s3 = float(input('Ingrese la longitud del lado n°3: '))

triangle_area = triangle_area(s1, s2, s3)
print('El área del triangulo es', triangle_area)
