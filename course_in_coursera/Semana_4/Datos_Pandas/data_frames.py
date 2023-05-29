import pandas as pd

# CREAR
# Con diccionarios
a1 = {"tiempo": 9.58, "atleta": "Usain", "pais": "Jamaica", "fecha": "16/08/2009", "ciudad": "Berlin"}
a2 = {"tiempo": 9.69, "atleta": "Usain", "pais": "Jamaica", "fecha": "16/09/2008", "ciudad": "Beijin"}
a3 = {"tiempo": 9.72, "atleta": "Usain", "pais": "Jamaica", "fecha": "31/05/2008", "ciudad": "New York"}
a4 = {"tiempo": 9.74, "atleta": "Asafa", "pais": "Jamaica", "fecha": "09/09/2007", "ciudad": "Riete"}
a5 = {"tiempo": 9.77, "atleta": "Asafa", "pais": "Jamaica", "fecha": "18/08/2006", "ciudad": "Zurich"}

records = [a1, a2, a3, a4, a5]
df_records = pd.DataFrame(records)
print(df_records)

# Con listas
tiempos = []
atletas = []
paises = []
fechas = []
ciudades = []

datos = {"tiempo": tiempos, "atleta": atletas, "pais": paises, "fecha": fechas, "ciudad": ciudades}
df_records2 = pd.DataFrame(datos)
