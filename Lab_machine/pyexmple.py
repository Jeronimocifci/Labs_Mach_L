import numpy as np
from scipy.optimize import minimize

# 1) Función objetivo: NEGATIVA de lo que deseamos maximizar
def funcion_objetivo(X):
    x_R, x_C, x_P, x_A = X
    return -(40*x_R + 250*x_C + 30*x_P + 5*x_A)  
    # Al minimizar esto, equivalemos a maximizar la utilidad original.

# 2) Definir funciones de restricción => deben retornar un valor >= 0

# 7x_R + 10x_C + 2x_P +  x_A <= 325  =>  325 - (... ) >= 0
def c1(X):
    x_R, x_C, x_P, x_A = X
    return 325 - (7*x_R + 10*x_C + 2*x_P + x_A)

#  x_R + 2.5x_C + 0.5x_P <= 55      =>  55 - (... ) >= 0
def c2(X):
    x_R, x_C, x_P, x_A = X
    return 55 - (x_R + 2.5*x_C + 0.5*x_P)

# 5x_R + 7x_C + 2x_P + 7x_A <= 420  =>  420 - (... ) >= 0
def c3(X):
    x_R, x_C, x_P, x_A = X
    return 420 - (5*x_R + 7*x_C + 2*x_P + 7*x_A)

# 50x_R + 88x_C + 27x_P + 50x_A <= 3800 => 3800 - (... ) >= 0
def c4(X):
    x_R, x_C, x_P, x_A = X
    return 3800 - (50*x_R + 88*x_C + 27*x_P + 50*x_A)

# Mínimos de variables:
# x_R >= 15 => x_R - 15 >= 0
def c5(X):
    x_R, x_C, x_P, x_A = X
    return x_R - 15

# x_C >= 10 => x_C - 10 >= 0
def c6(X):
    x_R, x_C, x_P, x_A = X
    return x_C - 10

# x_P >= 20 => x_P - 20 >= 0
def c7(X):
    x_R, x_C, x_P, x_A = X
    return x_P - 20

# x_A >= 0  => x_A - 0 >= 0
def c8(X):
    x_R, x_C, x_P, x_A = X
    return x_A - 0

# 3) Construir la lista total de restricciones
constraints = [
    {"type": "ineq", "fun": c1},
    {"type": "ineq", "fun": c2},
    {"type": "ineq", "fun": c3},
    {"type": "ineq", "fun": c4},
    {"type": "ineq", "fun": c5},
    {"type": "ineq", "fun": c6},
    {"type": "ineq", "fun": c7},
    {"type": "ineq", "fun": c8}
]

# 4) Punto inicial factible (minimos)
x0 = np.array([15, 10, 20, 0])

# 5) Llamamos a minimize()
resultado = minimize(funcion_objetivo,
                     x0,
                     method='SLSQP',
                     constraints=constraints)

# 6) Mostrar el resultado
print("Éxito:", resultado.success)
print("Mensaje:", resultado.message)
print("Valor máximo de la función objetivo:", -resultado.fun)  # Con signo menos
print("Variables óptimas [x_R, x_C, x_P, x_A]:", resultado.x)
