# Queremos crear un programa que nos permita contabilizar los votos de las elecciones presidenciales de los Estados
# Unidos. Para representar los votos, se ha decidido utilizar una lista de tuplas, donde cada voto es representado
# por una tupla, que incluye un identificador único de voto, el nombre del candidato por quién se ha votado, el
# estado del cual provienen el voto y el condado dentro del estado al que pertenece el voto. Aquí podemos ver unos
# ejemplos de las tuplas que podemos encontrar en las listas. De cómo se vería un voto para cada unos de los
# principales candidatos, teniendo en cuenta su estructura para manejar la información, se desea poder conocer.
# Primero la cantidad de votos recibidos por cada candidato en un determinado estado del país. Esta información
# se debe retornar como una tupla. Segundo se quiere poder conocer la cantidad de votos recibidos por cada candidato,
# en cada uno de los 50 estados del país. La información debe retornar se en un diccionario, cuyas llaves son los
# nombres de los estados y los valores son tuplas con la cantidad de votos recibidos por cada candidato en el estado

def votos_por_candidato(votos_a_validar: list, estado_a_analizar: str) -> tuple:
    votos_petro = 0
    votos_fico = 0
    for voto in votos_a_validar:
        if voto[2] == estado_a_analizar:
            if voto[1] == 'Petro':
                votos_petro += 1
            else:
                votos_fico += 1
    return votos_petro, votos_fico


def votos_por_estado(votos_a_validar: list, lista_estados: tuple) -> dict:
    votos_estados = {}
    for estado_actual in lista_estados:
        votos_estados[estado_actual] = votos_por_candidato(votos_a_validar, estado_actual)
    return votos_estados


votos = [
    ('A1', 'Petro', 'Antioquia', 'Bello'),
    ('A2', 'Petro', 'Cundinamarca', 'Bogota'),
    ('A3', 'Petro', 'Nariño', 'Pasto'),
    ('A4', 'Petro', 'Antioquia', 'Medellín'),
    ('A5', 'Petro', 'Antioquia', 'Medellín'),
    ('A6', 'Fico', 'Valle del cauca', 'Cali'),
    ('A7', 'Petro', 'Antioquia', 'Sabaneta'),
    ('A8', 'Fico', 'Antioquia', 'Itagui'),
    ('A9', 'Petro', 'Nariño', 'Pasto'),
    ('A10', 'Fico', 'Cundinamarca', 'Bogota'),
    ('A11', 'Petro', 'Valle del cauca', 'Cali')
]
estados = ('Antioquia', 'Cundinamarca', 'Nariño', 'Valle del cauca')

estado = input('¿Cuál es el estado a analizar? ')
print(votos_por_candidato(votos, estado))
print(votos_por_estado(votos, estados))
