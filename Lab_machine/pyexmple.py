import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x)
def f(x):
    return np.sin(x) + np.sin((10/3) * x)

# Definir el rango de x
x_values = np.linspace(2.7, 7.5, 500)
y_values = f(x_values)

# Condiciones iniciales dadas
initial_conditions = [3.0, 3.1, 3.2, 3.3]

# Calcular los valores de x[k] con una regla arbitraria (por ejemplo, sucesión de puntos espaciados)
x_k_values = {}
for x0 in initial_conditions:
    x_k_values[x0] = [x0]
    for _ in range(20):  # Generar 20 valores
        x_k_values[x0].append(x_k_values[x0][-1] + 0.2)  # Paso arbitrario

# Graficar la función
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="f(x) = sin(x) + sin(10x/3)", color="black")

# Colores para cada condición inicial
colors = ['red', 'blue', 'green', 'purple']

# Graficar los puntos generados con cada condición inicial
for i, x0 in enumerate(initial_conditions):
    x_k = np.array(x_k_values[x0])
    y_k = f(x_k)
    plt.scatter(x_k, y_k, color=colors[i], label=f"x[0] = {x0}")

# Configurar la gráfica
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica de f(x) y puntos generados con diferentes condiciones iniciales")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()