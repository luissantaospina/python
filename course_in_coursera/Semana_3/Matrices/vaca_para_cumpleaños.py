# Una clase de estudiantes ejemplares ha decidido hacer una vaca para el cumpleaños
# de su profesor favorito. Para esto, un estudiante recorrerá _todo el salón recogiendo
# el dinero que cada estudiante va a aportar. Tienen dos opciones de regalo: una botella
# de licor que cuesta 120.000 o un pastel que cuesta 35.000. Además, el estudiante que
# más dinero ponga, será el que tenga el honor de darle el regalo al profesor.
# Recree este caso en una función que reciba una matriz que representa al salón y
# una cadena que indica el regalo. Debe retornar una lista cuya primera posición es
# un mensaje que indica si el dinero alcanzó para la vaca y las siguientes dos posiciones
# son las coordenadas del puesto del estudiante que más aportó.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
# Nombre de la función: hacer_la_vaca
# Si lo requiere, puede agregar funciones adicionales.


def hacer_la_vaca(salon_aporte: list, tipo_vaca: str) -> list:
    resultado = []
    maximo_aporte = 0
    posicion_maximo_aporte = 0
    sumatoria = 0
    for i in range(len(salon_aporte)):
        sumatoria += salon_aporte[i][1]
        if salon_aporte[i][1] > maximo_aporte:
            maximo_aporte = salon_aporte[i][1]
            posicion_maximo_aporte = i
    if tipo_vaca == 'botella' and sumatoria >= 120000 or tipo_vaca == 'pastel' and sumatoria >= 35000:
        resultado.append('Hay Vaca')
    else:
        resultado.append('No Alcanza')
    resultado.append(posicion_maximo_aporte)
    return resultado


salon = [
    ['luis', 80000],
    ['daniela', 20000],
    ['andres', 100000],
    ['juan', 25000],
    ['carlos', 25000]
]

vaca = 'botella'

print(hacer_la_vaca(salon, vaca))
