import functools    # Libreria para trabajar con funciones


def plus_numbers(function):
    @functools.wraps(function)    # Permite que no se pierda la referencia a la función principal
    def wrapper(*args) -> None:
        return sum(args)

    return wrapper


@plus_numbers
def main(*args):
    return args


print(main(1, 2, 3))
print(main.__name__)
print(plus_numbers.__name__)
