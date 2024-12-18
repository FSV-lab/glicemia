import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datos
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Crear el gráfico de violín
sns.violinplot(data=data)

# Títulos y etiquetas
plt.title("Gráfico de Violín")
plt.xlabel("Categorías")
plt.ylabel("Distribución")

# Mostrar el gráfico
plt.show()
