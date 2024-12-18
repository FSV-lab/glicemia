# Reimportar la biblioteca y recrear el gráfico después del reinicio del estado
import matplotlib.pyplot as plt

# Datos para el gráfico circular actualizado
generos_principales = ['Ficción', 'No Ficción', 'Infantil y Juvenil', 'Otros Géneros']
ventas_principales = [40, 35, 20, 5]

# Crear el gráfico circular para las ventas por género principal
plt.figure(figsize=(8, 8))
colors_principales = plt.cm.Paired(range(len(generos_principales)))  # Generar colores desde el mapa de colores
plt.pie(ventas_principales, labels=generos_principales, autopct='%1.1f%%', startangle=140, colors=colors_principales)
plt.title('Ventas por Género Principal')
plt.show()
