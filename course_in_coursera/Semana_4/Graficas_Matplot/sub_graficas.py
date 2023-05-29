import matplotlib.pyplot as plt

meses = [
    'Ene', 'Feb', 'Maz', 'Abr',
    'May', 'Jun', 'Jul', 'Ago',
    'Sep', 'Oct', 'Nov', 'Dic'
]
temperaturas = [
    [12, 13, 14, 67, 67, 89, 90, 12, 34, 53, 12, 34],
    [1, 13, 14, 6, 67, 89, 9, 12, 34, 5, 26, 3],
    [16, 13, 14, 63, 67, 30, 9, 12, 34, 5, 2, 3],
    [1, 13, 14, 63, 67, 20, 10, 12, 34, 53, 26, 33],
    [13, 13, 14, 6, 67, 89, 9, 12, 34, 5, 26, 3],
    [11, 13, 14, 15, 16, 9, 19, 12, 34, 40, 21, 31]
]
ciudades = [
    'Medellín', 'Bogotá', 'Cali',
    'Valledupar', 'Cartagena', 'Pasto'
]

grafica, axes = plt.subplots(2, 3, figsize=(12, 8), sharex=True, sharey=True)
ciudad = 0
for fila in axes:
    for ax in fila:
        ax.plot(meses, temperaturas[ciudad], 'r', label='temperatura')
        ax.set_xticklabels(meses)
        ax.set_xlabel('Meses')
        ax.set_ylabel('Temperaturas', color='red')
        ax.set_title(ciudades[ciudad])
        ciudad += 1

plt.tight_layout()
grafica.show()
