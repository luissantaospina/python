n = int(input('Ingrese un numero (n): '))
d = int(input('Ingrese un numero (d): '))


def es_divisible(n: int, d: int) -> int:
    if n % (2 * d) == 0:
        variable = 2
    elif n % d == 0:
        variable = 1
    else:
        variable = 0
    return variable


print(es_divisible(n, d))
