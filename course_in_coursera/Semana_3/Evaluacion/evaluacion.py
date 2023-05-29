# 1

def funcion(x: int, n: int) -> int:
    result = 1
    i = n * x
    while i >= 0:
        result *= i**x
        i -= 1
    return result


print(funcion(2, 5))
