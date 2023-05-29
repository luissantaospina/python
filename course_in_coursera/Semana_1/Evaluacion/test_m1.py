# Question
variable_1 = '4'
variable_2 = int(str(variable_1))
variable_3 = variable_1*2
variable_1 = variable_2*2
variable_2 = variable_1
variable_1 = str(float(variable_2))

print(variable_1)

# Question
variable_1 = 1234
variable_2 = str(variable_1)
variable_3 = float(variable_1)
variable_1 = float(variable_1)
variable_2 = int(variable_1)
variable_3 = int(float(variable_1) + float(variable_2))

print(variable_3)

# Question


def vel_en_caida_libre(distancia: float) -> float:
    velocidad_inicial = 0
    aceleracion = 9.8
    vf = pow((pow(velocidad_inicial, 2) + 2 * aceleracion * distancia), 0.5)
    return vf


altura = 1.2
print('la velocidad es', round(vel_en_caida_libre(altura), 2))
