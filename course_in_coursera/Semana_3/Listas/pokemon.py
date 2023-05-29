# Ash Ketchum, el personaje principal del anime Pokémon, está a punto de luchar en la final de la
# liga Kalos. En estos eventos compiten los mejores entrenadores del mundo en batallas donde cada
# entrenador puede tener 3, 4, 5 o 6 criaturas. Ash quiere saber, para una cantidad de criaturas específica,
# si él podrá formar un equipo únicamente con Pokémon seudolegendarios para competir en la final.
# Un pokemon seudolegendario es aquel que en la suma de sus estadísticas de combate tiene 600 puntos o más.
#
# Las estadísticas de combate de cada pokemon son 6:
# "ataque"
# "defensa"
# "ataque_especial"
# "defensa_especial"
# "velocidad"
# "vida"
#
# Escriba una función que, dada una lista de diccionarios (cada uno representando un pokémon) con
# las anteriores estadísticas, determine si Ash podrá formar un equipo de pokémon seudolegendarios
# para afrontar la final de la liga. En caso que Ash pueda formar un equipo, retorne una lista con
# los nombres de las criaturas que Ash utilizaría en la batalla. Si es imposible generar un equipo
# que cumpla con las condiciones, retorne None.
#
# Se garantiza que en caso de poder formar un equipo válido, solamente habrá una configuración posible.
#
# La lista de retorno debe componerse únicamente de cadenas de caracteres y debe tener el mismo orden
# de la lista que llega por parámetro.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: construir_equipo_pokemon
# Si lo requiere, puede agregar funciones adicionales.


def construir_equipo_pokemon(cantidad_pokemones: int, lista_pokemones: list) -> list:
    pokemonos_a_pelear = []
    for pokemon in lista_pokemones:
        suma_combate = pokemon['ataque'] + pokemon['defensa'] + pokemon['ataque_especial'] + \
                       pokemon['defensa_especial'] + pokemon['velocidad'] + pokemon['vida']
        if suma_combate >= 600:
            pokemonos_a_pelear.append(pokemon['nombre'])
    if len(pokemonos_a_pelear) < cantidad_pokemones:
        pokemonos_a_pelear = None
    return pokemonos_a_pelear


pokemones = [
    {
        'nombre': 'pikachu',
        'ataque': 100,
        'defensa': 200,
        'ataque_especial': 100,
        'defensa_especial': 400,
        'velocidad': 150,
        'vida': 100
    },
    {
        'nombre': 'bulbasaur',
        'ataque': 100,
        'defensa': 100,
        'ataque_especial': 100,
        'defensa_especial': 500,
        'velocidad': 100,
        'vida': 50
    },
    {
        'nombre': 'charmander',
        'ataque': 100,
        'defensa': 100,
        'ataque_especial': 100,
        'defensa_especial': 30,
        'velocidad': 100,
        'vida': 100
    },
    {
        'nombre': 'charizard',
        'ataque': 150,
        'defensa': 100,
        'ataque_especial': 100,
        'defensa_especial': 20,
        'velocidad': 100,
        'vida': 400
    }
]

numero_pokemones = int(input('Ingrese la cantidad de pokemones con los que desea pelear: '))
print(construir_equipo_pokemon(numero_pokemones, pokemones))
