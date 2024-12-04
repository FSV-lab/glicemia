import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk  # Asegúrate de importar mplcyberpunk

# Aplica el estilo 'cyberpunk' a Matplotlib
plt.style.use('cyberpunk')

# Variables actualizadas
x = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
y = [50, 60, 70, 80, 90, 100, 110]  # Ajustar para que coincida con los días de la semana

# Gráfico con estilo 'cyberpunk'
fig, ax = plt.subplots()
ax.plot(x, y, 'aqua', marker='o', linewidth=2)

# Agrega efectos adicionales de mplcyberpunk
mplcyberpunk.make_lines_glow(ax)
mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.6)

# Agregar etiquetas y título
ax.set_title('Datos Semanales Glicemia')
ax.set_xlabel('Días de la Semana')
ax.set_ylabel('Glucosa')

plt.show()

