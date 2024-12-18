import matplotlib.pyplot as plt
import numpy as np

# Datos
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Crear el gráfico de caja
plt.boxplot(data, patch_artist=True, notch=True, 
            boxprops=dict(facecolor='lightblue', color='blue'),
            capprops=dict(color='blue'),
            whiskerprops=dict(color='blue'),
            flierprops=dict(color='red', markeredgecolor='red'),
            medianprops=dict(color='black'))

# Títulos y etiquetas
plt.title("Gráfico de Caja con Múltiples Categorías")
plt.xlabel("Categorías")
plt.ylabel("Valores")

# Mostrar el gráfico
plt.show()
