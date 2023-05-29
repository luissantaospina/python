import calculadora_indices as calc

peso = float(input('Ingrese el peso en kilogramos: '))
altura = float(input('Ingrese la altura en metros: '))

print('Su indice de masa corporal es', round(calc.calcular_imc(peso, altura), 2))
