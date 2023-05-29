# noinspection PyUnresolvedReferences
import matplotlib.image as mpimg
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt


def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R,G,B) que representan la imagen a visualizar.
    """
    alto = len(imagen)
    ancho = len(imagen[0])

    # Construir una matriz para representar la imagen.
    # Esta matriz tendrá tres dimensiones
    matriz = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            # convertir la tupla a una lista
            r, g, b = imagen[i][j]
            fila.append([r, g, b])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()


def cargar_imagen(ruta_imagen: str) -> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxN con tuplas (R,G,B).
    """
    matriz = mpimg.imread(ruta_imagen).tolist()
    alto = len(matriz)
    ancho = len(matriz[0])

    # Construir una matriz para representar la imagen.
    # Esta matriz tendrá dos dimensiones y tuplas en cada casilla.
    imagen = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            # Extraer los componentes. Note que no se puede desempaquetar.
            r = matriz[i][j][0]
            g = matriz[i][j][1]
            b = matriz[i][j][2]

            # Construir la tupla equivalente y agregarla a la imagen
            tupla = (r, g, b)
            fila.append(tupla)
        imagen.append(fila)
    return imagen


def convertir_a_grises(imagen_a_convertir: list) -> None:
    ancho = len(imagen_a_convertir[0])
    alto = len(imagen_a_convertir)
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen_a_convertir[i][j]
            gris = (rojo + verde + azul) // 3
            imagen_a_convertir[i][j] = (gris, gris, gris)


def convertir_a_binario(imagen: list, umbral: int) -> None:
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen[i][j]
            gris = (rojo + verde + azul) // 3
            if gris < umbral:
                imagen[i][j] = (0, 0, 0)
            else:
                imagen[i][j] = (255, 255, 255)


imagen_muestra = cargar_imagen("muestra.jpg")
visualizar_imagen(imagen_muestra)
convertir_a_grises(imagen_muestra)
visualizar_imagen(imagen_muestra)
convertir_a_binario(imagen_muestra, 100)
visualizar_imagen(imagen_muestra)
