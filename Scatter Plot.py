import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 4, 6, 8]

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Títulos y etiquetas
plt.title("Gráfico de Dispersión")
plt.xlabel("X")
plt.ylabel("Y")

# Mostrar el gráfico
plt.show()
