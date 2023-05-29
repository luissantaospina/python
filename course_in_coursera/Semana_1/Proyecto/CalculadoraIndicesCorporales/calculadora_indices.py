def calcular_imc(peso: float, altura: float) -> float:
    imc = peso / pow(altura, 2)
    return imc


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    imc = calcular_imc(peso, altura)
    gc = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero
    return gc


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int,
                                   valor_actividad: float) -> float:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    tmb_actividad_fisica = tmb * valor_actividad
    return tmb_actividad_fisica


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_min = tmb * 0.8
    calorias_max = tmb * 0.85
    return 'Para adelgazar es recomendado que consumas entre: ' + str(round(calorias_min, 2)) + ' y ' \
           + str(round(calorias_max, 2)) + ' calorías al día.'
