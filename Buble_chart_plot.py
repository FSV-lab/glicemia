import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]
sizes = [100, 200, 300, 400, 500]  # Tamaño de las burbujas
colors = [50, 100, 150, 200, 250]  # Color de las burbujas

# Crear el gráfico de burbujas
plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.6, edgecolors="w", linewidth=2)

# Títulos y etiquetas
plt.title("Gráfico de Dispersión con Colores y Tamaños")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label="Color Intensity")

# Mostrar el gráfico
plt.show()
