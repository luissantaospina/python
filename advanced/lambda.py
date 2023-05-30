from functools import reduce


# Lambda
square = lambda x: x ** 2

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

# Lambda with filter
values = [2, 65, 67, 78, 98]
peers = list(filter(lambda x: x % 2 == 0, values))

# Lambda with reduce
values_reduce = [2, 65, 67, 78, 98]
sum_values = reduce(lambda x, y: x + y, values_reduce)
print(sum_values)
