import matplotlib.pyplot as plt

# Datos para el gráfico circular (ventas anuales por género)
generos = ['Fantasy', 'Mystery', 'Romance', 'Historical']
ventas_anuales = [102000, 92000, 124000, 60000]

# Crear el gráfico circular
plt.figure(figsize=(8, 8))
colors = plt.cm.Paired(range(len(generos)))  # Generar colores desde el mapa de colores
plt.pie(ventas_anuales, labels=generos, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribución de Ventas Anuales por Género')
plt.show()
