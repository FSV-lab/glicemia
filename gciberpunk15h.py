import matplotlib.pyplot as plt
import mplcyberpunk

# Datos extraídos de la tabla
fechas = [
    "11/10/2024", "11/10/2024", "12/10/2024", "12/10/2024", "13/10/2024", 
    "14/10/2024", "14/10/2024", "15/10/2024", "15/10/2024", "16/10/2024",
    "16/10/2024", "17/10/2024", "17/10/2024", "18/10/2024", "18/10/2024",
    "19/10/2024", "19/10/2024", "20/10/2024", "20/10/2024", "21/10/2024", 
    "21/10/2024", "22/10/2024", "22/10/2024", "23/10/2024", "23/10/2024", 
    "24/10/2024", "24/10/2024"
]
horas = [
    "12:00", "15:00", "15:00", "18:00", "2:00", "8:00", "11:00", "10:00", 
    "15:15", "14:00", "17:00", "8:00", "10:00", "12:00", "14:00", "10:00", 
    "19:00", "2:00", "19:00", "8:00", "10:00", "12:00", "14:00", "14:00", 
    "19:00", "8:00", "11:00"
]
valores_glucosa = [
    148, 161, 107, 186, 240, 177, 313, 203, 315, 215, 316, 176, 241, 284, 303,
    141, 238, 203, 193, 278, 194, 153, 345, 207, 234, 216, 301
]

# Crear un índice de tiempo combinando fecha y hora
x = [f"{fecha} {hora}" for fecha, hora in zip(fechas, horas)]
y = valores_glucosa

# Configurar la gráfica
plt.style.use("cyberpunk")
plt.figure(figsize=(14, 8))

# Graficar
plt.plot(x, y, marker='o', label="Nivel de glucosa")

# Configurar estilo y etiquetas
plt.title("Niveles de Glucosa", fontsize=20)
plt.xlabel("Tiempo (Fecha y Hora)", fontsize=12)
plt.ylabel("Nivel de Glucosa (mg/dL)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend()

# Efectos de ciberpunk
mplcyberpunk.add_glow_effects()

# Mostrar gráfica
plt.tight_layout()
plt.show()
