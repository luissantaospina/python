# Cree una función que pueda calcular el índice de masa corporal (BMI) de una persona.
#
# La fórmula para calcular el BMI es la siguiente:
#
# BMI = peso/(altura^2)
#
# En esta fórmula el peso está en kilogramos y la altura en metros.
# Tenga en cuenta que el peso y altura que reciban su función,
# van a estar en libras y pulgadas respectivamente, ya que su función será usada en los Estados Unidos.
#
# Recuerde que:
#
# 1 libra corresponde a 0.45 kg.
#
# 1 pulgada corresponde a 0.025 metros.
#
# El valor de retorno debe estar redondeado a dos decimales.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: calcular_BMI
#
# Si lo requiere, puede agregar funciones adicionales.


def calculate_bmi(height: float, weight: float) -> float:
    height = height * 0.025
    weight = weight * 0.45
    bmi = round(weight/(pow(height, 2)), 2)
    return bmi


h_inch = float(input('Ingrese su altura en pulgadas: '))
w_lb = float(input('Ingrese su peso en libras: '))

print('Su indice de masa corporal es', calculate_bmi(h_inch, w_lb))
