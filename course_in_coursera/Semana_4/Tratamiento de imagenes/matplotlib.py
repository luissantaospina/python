# noinspection PyUnresolvedReferences
import matplotlib.image as mpimg
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt


def cargar_imagen_matriz(ruta_imagen: str) -> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxNx3
    """
    imagen = mpimg.imread(ruta_imagen)
    return imagen


def visualizar_imagen_matriz(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxNx3 que representa la imagen a visualizar.
    """
    plt.imshow(imagen)
    plt.show()


imagen_muestra = cargar_imagen_matriz("muestra.jpg")
visualizar_imagen_matriz(imagen_muestra)
