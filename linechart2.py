import matplotlib.pyplot as plt

# Datos para el gráfico de líneas (ventas anuales por género)
generos = ['Fantasy', 'Mystery', 'Romance', 'Historical']
ventas_anuales = [102000, 92000, 124000, 60000]

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(generos, ventas_anuales, marker='o', linestyle='-', color='b', label='Ventas Anuales')
plt.title('Ventas Anuales por Género', fontsize=14)
plt.xlabel('Género', fontsize=12)
plt.ylabel('Ventas (en unidades)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
