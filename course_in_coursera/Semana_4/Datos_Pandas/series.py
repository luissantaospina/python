import pandas as pd

# CREAR
# Sin index
datos = [2, 8, 9, 67, 78]
temp1 = pd.Series(datos, name='Tem')
# Con index
datos = [2, 8, 9, 67, 78]
fechas = ['2/3', '5/3', '8/3', '9/3', '15/3']
temp2 = pd.Series(datos, index=fechas, name='Tem')
# Con diccionarios
datos = {
    2: '2/3',
    8: '2/4',
    9: '2/9'
}
temp3 = pd.Series(datos, name='Tem')

# EXTRAER VALORES
num1 = [2, 3, 4, 5, 6]
num2 = [21, 84, 97, 67, 78]
serie = pd.Series(num2, index=num1, name='Serie')

print(serie)
print(serie.get(5))  # Por indice, retorna numero
print(serie.loc[2:4])  # Conjunto por índice, retorna seria con el inicio y el fin incluidos
print(serie.iloc[2:4])  # Conjunto por posiciones (0 - 1), retorna seria sin incluir el inicio

print(serie.values)  # Retorna los valores
print(serie.to_list())  # Retorna los valores en una lista
copia = serie.copy()  # Copia una serie

# OPERACIONES
indice = [1, 3, 4, 5, 6]
num3 = [21, 84, 97, 67, 78]
serie1 = pd.Series(num3, index=indice, name='Serie')
num4 = [21, 84, 97, 67, 78]
serie2 = pd.Series(num4, name='Serie')

print(serie1)
print(serie1 + serie2)  # Suma los valores con el mismo indicé,
# si no se tiene un indicé en ambas series esto traera un valor NaN

print(serie1.add(serie2, fill_value=0))  # Suma los valores con el mismo indicé,
# si no se tiene un indicé en ambas series esto completa el valor con el fill_value
serie1.max()  # Calcula el maxim
serie1.min()  # Calcula el minimo
serie1.mean()  # Calcula el promedio
serie1.std()  # Calcula la desviación estandar
serie1.median()  # Calcula la mediana
