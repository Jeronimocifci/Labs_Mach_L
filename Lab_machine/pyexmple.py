import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de t
t = np.linspace(0.5, 3.0, 30)

# Definir las funciones
f_t = np.log(t**2)       # Función logarítmica
g_t = np.exp(-t) / t     # Función exponencial
suma_t = f_t + g_t       # Suma de funciones
compuesta_t = np.log(g_t**2)  # Función compuesta

# Crear la figura y los subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Gráfico 1: Logarítmica
axs[0, 0].plot(t, f_t, label=r'$f(t) = \ln(t^2)$', color='b')
axs[0, 0].set_title("Logarítmica")
axs[0, 0].set_xlabel("Tiempo (s)")
axs[0, 0].set_ylabel("Distancia (m)")
axs[0, 0].legend()
axs[0, 0].grid()

# Gráfico 2: Exponencial
axs[0, 1].plot(t, g_t, label=r'$g(t) = \frac{e^{-t}}{t}$', color='g')
axs[0, 1].set_title("Exponencial")
axs[0, 1].set_xlabel("Tiempo (s)")
axs[0, 1].set_ylabel("Distancia (m)")
axs[0, 1].legend()
axs[0, 1].grid()

# Gráfico 3: Suma
axs[1, 0].plot(t, suma_t, label=r'$f(t) + g(t)$', color='r')
axs[1, 0].set_title("Suma")
axs[1, 0].set_xlabel("Tiempo (s)")
axs[1, 0].set_ylabel("Distancia (m)")
axs[1, 0].legend()
axs[1, 0].grid()

# Gráfico 4: Compuesta
axs[1, 1].plot(t, compuesta_t, label=r'$f(g(t))$', color='m')
axs[1, 1].set_title("Compuesta")
axs[1, 1].set_xlabel("Tiempo (s)")
axs[1, 1].set_ylabel("Distancia (m)")
axs[1, 1].legend()
axs[1, 1].grid()

# Título general de la figura
fig.suptitle("Gráficas de Funciones Matemáticas", fontsize=14)

# Ajustar los subplots para mejor presentación
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Mostrar la gráfica
plt.show()