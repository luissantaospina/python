import matplotlib.pyplot as plt

meses = [
    'Ene', 'Feb', 'Maz', 'Abr',
    'May', 'Jun', 'Jul', 'Ago',
    'Sep', 'Oct', 'Nov', 'Dic'
]
temperaturas = [
    12, 13, 14, 67, 67, 89,
    90, 12, 34, 53, 12, 34
]

grafica = plt.figure(figsize=(9, 5))
ax = grafica.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(meses, temperaturas, 'r', label='temperatura')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperaturas', color='red')
ax.set_title('Temperaturas y precipitación promedio en Bogotá, por mes (1970-2000)')
plt.show()
