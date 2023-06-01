# * -> Lista
# _ -> Omitir valores

# Desempaqueta la tupla con los primeros tres números y el resto lo guarda en la variable
numeros = (1, 2, 3, 4, 5, 6, 7, 8)
uno, dos, tres, *resto_numeros = numeros
print(uno, dos, tres, resto_numeros)

# Desempaqueta la tupla con los primeros tres números y el resto lo guarda en la variable
numeros_dos = (4, 5, 6, 7, 8)
cuatro, cinco, *_ = numeros_dos
print(cuatro, cinco)

# Desempaqueta la tupla con los primeros tres números, el resto lo guarda en la variable y el último lo guarda
numeros_dos = (6, 7, 8, 9, 10, 11)
seis, siete, *_, once = numeros_dos
print(seis, siete, once)
