import matplotlib.pyplot as plt

# Datos
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Crear el histograma
plt.hist(data, bins=5, edgecolor='black')

# Títulos y etiquetas
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")

# Mostrar el gráfico
plt.show()
