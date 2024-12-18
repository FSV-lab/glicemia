import matplotlib.pyplot as plt

# Datos
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Crear el gráfico de barras
plt.bar(categories, values)

# Títulos y etiquetas
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")

# Mostrar el gráfico
plt.show()
