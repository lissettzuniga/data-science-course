import pandas as pd
import matplotlib.pyplot as plt

# URL del dataset
url = "https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv"

# Cargar datos
datos = pd.read_csv(url, sep=';')

# Tipos de inmuebles comerciales que queremos eliminar
inmuebles_comerciales = [
    'Conjunto Comercial/Sala', 'Edificio Completo', 'Tienda/Salón',
    'Casa Comercial', 'Terreno Estándar', 'Cochera/Estacionamiento',
    'Galpón/Depósito/Almacén', 'Tienda en Centro Comercial',
    'Hotel', 'Loteo/Condominio', 'Industria'
]

# Filtrar dataframe
df = datos.query('@inmuebles_comerciales not in Tipo')

# ------------------------------
# Promedio de habitaciones
# ------------------------------
promedio_habitaciones = df['Habitaciones'].mean()

print("Promedio de habitaciones:")
print(promedio_habitaciones)

# ------------------------------
# Promedio de alquiler por colonia
# ------------------------------
promedio_colonia = (
    df.groupby('Colonia')[['Valor']]
    .mean()
    .sort_values('Valor', ascending=False)
)

print("\nColonias con mayor promedio de alquiler:")
print(promedio_colonia)

# ------------------------------
# Top 5 colonias más caras
# ------------------------------
top5_colonias = promedio_colonia.head()

print("\nTop 5 colonias con alquiler más alto:")
print(top5_colonias)


top5_colonias.plot(kind='bar')
plt.title("Top 5 colonias con mayor alquiler promedio")
plt.ylabel("Valor promedio")
plt.show()