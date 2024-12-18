import matplotlib.pyplot as plt

# Datos (asegúrate de ajustar los nombres de las categorías si son diferentes)
datos = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Annual'],
    'Fantasy': [30000, 27000, 26000, 19000, 102000],
    'Mystery': [25000, 18000, 22000, 27000, 92000],
    'Romance': [28000, 32000, 33000, 31000, 124000],
    'Historical': [15000, 16000, 18000, 11000, 60000]
}

# Extraer los datos en formato adecuado para matplotlib
quarters = datos['Quarter']
fantasy = datos['Fantasy']
mystery = datos['Mystery']
romance = datos['Romance']
historical = datos['Historical']

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Trazar las líneas para cada categoría
plt.plot(quarters, fantasy, label='Fantasy')
plt.plot(quarters, mystery, label='Mystery')
plt.plot(quarters, romance, label='Romance')
plt.plot(quarters, historical, label='Historical')

# Personalizar la gráfica
plt.xlabel('Quarter')
plt.ylabel('Valores Ganados')
plt.title('Valores Ganados por Categoría y Trimestre')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()