# Instance function and later use
def plus_one(number: int) -> int:
    return number + 1


funct = plus_one
funct(6)


# Pass function like arguments
def plus_numbers(number_1: int, number_2: int) -> int:
    return number_1 + number_2


def plus(numbers: funct) -> int:
    return numbers(6, 7)


sum_numbers = plus(plus_numbers)


# Return function and later use internal function
def hello() -> funct:
    def say_hi() -> str:
        name = 'Luis'
        return f'Hi {name}'
    return say_hi


hello_funct = hello()
hello_funct()
