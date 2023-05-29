import calculadora_indices as calc


def calcula_valor_genero() -> float:
    valida_genero = False
    valor_genero_calculado = 0
    while not valida_genero:
        genero = input('Ingrese la letra correspondiente a su genero\nM: Masculino\nF: Femenino\n')
        if genero == 'M' or genero == 'm':
            valor_genero_calculado = 10.8
            valida_genero = True
        elif genero == 'F' or genero == 'f':
            valor_genero_calculado = 0
            valida_genero = True
        else:
            print('El valor ingresado no es correcto, por favor rectifica')
    return valor_genero_calculado


peso = float(input('Ingrese el peso en kilogramos: '))
altura = float(input('Ingrese la altura en metros: '))
edad = int(input('Ingrese la edad en años: '))
valor_genero = calcula_valor_genero()

print('Su indice de masa corporal es ' + str(round(calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero), 2)) + '%')
