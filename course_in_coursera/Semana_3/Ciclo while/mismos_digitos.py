# Escriba una función que determine si en dos números enteros aparecen los mismos dígitos.
# No tenga en cuenta ni la frecuencia ni el orden de aparición de los dígitos en los números.
#
# Los números no tienen necesariamente la misma cantidad de dígitos. Por ejemplo,
# si los números son 998 y 89 la función debería retornar True.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: mismos_digitos
#
# Si lo requiere, puede agregar funciones adicionales.


def mismos_digitos(numero_1: int, numero_2: int) -> bool:
    tiene_mismos_digitos = False
    contador_encontro_digitos_uno_en_dos = 0
    contador_encontro_digitos_dos_en_uno = 0
    mayor_digitos = max(len(str(numero_1)), len(str(numero_2)))
    for i in range(mayor_digitos):
        if i < len(str(numero_1)) and str(numero_2).find(str(numero_1)[i]) >= 0:
            contador_encontro_digitos_uno_en_dos += 1
        if i < len(str(numero_2)) and str(numero_1).find(str(numero_2)[i]) >= 0:
            contador_encontro_digitos_dos_en_uno += 1

        if len(str(numero_1)) == contador_encontro_digitos_uno_en_dos and \
                len(str(numero_2)) == contador_encontro_digitos_dos_en_uno:
            tiene_mismos_digitos = True
    return tiene_mismos_digitos


numero_uno = int(input('Ingrese el numero 1: '))
numero_dos = int(input('Ingrese el numero 2: '))
print(mismos_digitos(numero_uno, numero_dos))
