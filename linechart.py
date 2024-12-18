import matplotlib.pyplot as plt

# Datos para el gráfico de líneas
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
ventas_ficcion = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]  # Ejemplo de datos de evolución mensual

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(meses, ventas_ficcion, marker='o', linestyle='-', color='blue', label='Ventas de Ficción')
plt.title('Evolución Mensual de Ventas de Ficción')
plt.xlabel('Meses')
plt.ylabel('Ventas (%)')
plt.xticks(rotation=45)  # Rotar etiquetas de los meses para mejor legibilidad
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
