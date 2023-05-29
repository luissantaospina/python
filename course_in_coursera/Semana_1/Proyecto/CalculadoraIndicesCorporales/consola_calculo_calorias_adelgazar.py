import calculadora_indices as calc


def calcula_valor_genero() -> int:
    valor_genero_calculado = 0
    while not valor_genero_calculado != 0:
        genero = input('Ingrese la letra correspondiente a su genero\nM: Masculino\nF: Femenino\n')
        if genero == 'M' or genero == 'm':
            valor_genero_calculado = 5
        elif genero == 'F' or genero == 'f':
            valor_genero_calculado = -161
        else:
            print('El valor ingresado no es correcto, por favor rectifica')
    return valor_genero_calculado


peso = float(input('Ingrese el peso en kilogramos: '))
altura = float(input('Ingrese la altura en centimetros: '))
edad = int(input('Ingrese la edad en años: '))
valor_genero = calcula_valor_genero()

print(calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero))


