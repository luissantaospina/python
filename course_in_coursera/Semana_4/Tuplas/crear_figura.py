# Su función debería recibir la imagen con una lista de diccionarios con la estructura que
# estudiamos y tendría que hacer solo pequeñas operaciones para recorrer la lista y los
# diccionarios e ir construyendo las cadenas correspondientes a cada figura.
# Reproduce el video desde :7:3 y sigue la transcripción7
# Como ayuda adicional, le recomendamos que construya una función auxiliar que reciba el
# diccionario de una figura y retorne la cadena SVG correspondiente a esa figura.


def crear_figura(posicion_figura: tuple,
                 tamano_figura: tuple,
                 grosor_borde_figura: str,
                 color_relleno_figura: str,
                 color_borde_figura: str) -> str:
    figura_nueva = {
        'posicion': posicion_figura,
        'tamano': tamano_figura,
        'esquina': (0, 0),
        'grosor_borde': grosor_borde_figura,
        'color_relleno': color_relleno_figura,
        'color_borde': color_borde_figura,
        'rotacion': (0, 0, 0)
    }
    return transformar_dict_a_svg(figura_nueva)


def transformar_dict_a_svg(figura: dict) -> str:
    svg = "<svg width='1000px' height='1000px' version='1.1' xmlns='http://www.w3.org/2000/svg'>" \
          "<rect fill='" + \
          figura['color_relleno'] + \
          "' height='" + \
          str(figura['tamano'][0]) + \
          "' rx='1' ry='1' stroke='" + \
          figura['color_borde'] + \
          "' stroke-width='" + \
          figura['grosor_borde'] + \
          "' transform='rotate(0,0,0)' width='" + \
          str(figura['tamano'][1]) + \
          "' x='0' y='0'/>" \
          "</svg>"
    return svg


posicion = (0, 0)
tamano = (600, 600)
grosor_borde = '6px'
color_relleno = '#92890E'
color_borde = '#6D76F1'
print(crear_figura(posicion, tamano, grosor_borde, color_relleno, color_borde))
