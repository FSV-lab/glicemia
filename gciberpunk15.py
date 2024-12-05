import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk

# Datos proporcionados en el formato de tabla
data = {
    'FECHA': ['11/10/2024', '11/10/2024', '12/10/2024', '12/10/2024', '13/10/2024', '14/10/2024', '14/10/2024', 
              '15/10/2024', '15/10/2024', '16/10/2024', '16/10/2024', '17/10/2024', '17/10/2024', '18/10/2024', 
              '18/10/2024', '19/10/2024', '19/10/2024', '20/10/2024', '20/10/2024', '21/10/2024', '21/10/2024', 
              '22/10/2024', '22/10/2024', '23/10/2024', '23/10/2024', '24/10/2024', '24/10/2024'],
    'HORA': ['12:00', '15:00', '15:00', '18:00', '02:00', '08:00', '11:00', '10:00', '15:15', '14:00', '17:00', 
             '08:00', '10:00', '12:00', '14:00', '10:00', '19:00', '02:00', '19:00', '08:00', '10:00', '12:00', 
             '14:00', '14:00', '19:00', '08:00', '11:00'],
    'GLUCOSA': [148, 161, 107, 186, 240, 177, 313, 203, 315, 215, 316, 176, 241, 284, 303, 141, 238, 203, 193, 278, 194, 
                153, 345, 207, 234, 216, 301]
}

df = pd.DataFrame(data)

# Combina FECHA y HORA en una sola columna 'Fecha-Hora' para el eje X
df['Fecha-Hora'] = pd.to_datetime(df['FECHA'] + ' ' + df['HORA'], dayfirst=True)

# Gráfico con estilo 'cyberpunk'
plt.style.use('cyberpunk')

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Fecha-Hora'], df['GLUCOSA'], color='aqua', marker='o', linewidth=2)

# Agregar efectos adicionales de mplcyberpunk
mplcyberpunk.make_lines_glow()
mplcyberpunk.add_gradient_fill()  # Sin parámetros adicionales

# Agregar etiquetas y título
ax.set_title('Datos de Glucosa Diarios', fontsize=16)
ax.set_xlabel('Fecha ', fontsize=12)
ax.set_ylabel('Nivel de Glucosa', fontsize=12)

# Mejorar la presentación de fechas en el eje X
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

