import matplotlib.pyplot as plt

# Datos
categories = ['A', 'B', 'C', 'D']
values_1 = [3, 6, 8, 5]
values_2 = [4, 7, 2, 6]
values_3 = [5, 3, 7, 2]

# Crear el gráfico de barras apiladas
plt.bar(categories, values_1, label='Serie 1', color='lightblue')
plt.bar(categories, values_2, label='Serie 2', bottom=values_1, color='orange')
plt.bar(categories, values_3, label='Serie 3', bottom=[i+j for i, j in zip(values_1, values_2)], color='green')

# Títulos y etiquetas
plt.title("Gráfico de Barras Apiladas")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.legend()

# Mostrar el gráfico
plt.show()
