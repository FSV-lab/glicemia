import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Crear el gráfico de área
plt.fill_between(x, y, color="skyblue", alpha=0.4)

# Títulos y etiquetas
plt.title("Gráfico de Área")
plt.xlabel("X")
plt.ylabel("Y")

# Mostrar el gráfico
plt.show()
