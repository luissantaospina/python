line_for_number = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 5
}

print(line_for_number)
print(line_for_number.keys())
print(line_for_number.values())
print(line_for_number.items())
print(line_for_number[8])
print(len(line_for_number))

# Eliminar un elemento por su llave
del line_for_number[0]
