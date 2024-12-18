import matplotlib.pyplot as plt

# Datos
data = [1, 2, 5, 6, 7, 8, 8, 9, 10, 10, 12]

# Crear el box plot
plt.boxplot(data)

# Títulos y etiquetas
plt.title("Gráfico de Caja y Bigotes")
plt.ylabel("Valores")

# Mostrar el gráfico
plt.show()
