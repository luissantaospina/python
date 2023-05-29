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
            print('El valor ingresado no es correcto')
    return valor_genero_calculado


def calcula_valor_actividad_fisica() -> float:
    valor_actividad_fisica = 0
    while not valor_actividad_fisica > 0:
        nivel_actividad_fisica = input('Ingrese el numero correspondiente a su nivel de actividad fisica'
                                       '\n1: poco o ningún ejercicio'
                                       '\n2: ejercicio ligero (1 a 3 días a la semana)'
                                       '\n3: ejercicio moderado (3 a 5 días a la semana)'
                                       '\n4: deportista (6 -7 días a la semana)'
                                       '\n5: atleta (entrenamientos mañana y tarde'
                                       '\n')
        match nivel_actividad_fisica:
            case '1': valor_actividad_fisica = 1.2
            case '2': valor_actividad_fisica = 1.375
            case '3': valor_actividad_fisica = 1.55
            case '4': valor_actividad_fisica = 1.725
            case '5': valor_actividad_fisica = 1.9
            case _: print('El valor ingresado no es correcto, por favor rectifica')

    return valor_actividad_fisica


peso = float(input('Ingrese el peso en kilogramos: '))
altura = float(input('Ingrese la altura en centimetros: '))
edad = int(input('Ingrese la edad en años: '))
valor_genero = calcula_valor_genero()
valor_actividad = calcula_valor_actividad_fisica()

print('Su tasa metabólica basal según actividad fisica (TMB) es:',
      round(calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad), 2)
      , 'cal')
