import matplotlib.pyplot as plt

# Datos
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Crear el gráfico circular
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Asegura que el gráfico es un círculo perfecto
plt.axis('equal')

# Mostrar el gráfico
plt.title("Gráfico Circular")
plt.show()
