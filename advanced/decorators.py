def uppercase_decorator(function):
    print("uppercase")

    def wrapper() -> None:
        make_uppercase = function().upper()
        return make_uppercase

    return wrapper


def lowercase_decorator(function):
    print("lowercase")

    def wrapper() -> None:
        make_lowercase = function().lower()
        return make_lowercase

    return wrapper


def split_string_decorator(function):
    print("split")

    def wrapper() -> None:
        splitted_string = function().split()
        return splitted_string

    return wrapper


@split_string_decorator
@lowercase_decorator
@uppercase_decorator
def say_hi():
    return "Hi Luis"


print(say_hi())
