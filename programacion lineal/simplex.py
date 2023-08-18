import cvxpy as cp

# Variables de decisión
x = cp.Variable()
y = cp.Variable()

# Función objetivo: Minimizar 2x + 3y
hola = 2*x + 4*y
objective = cp.Maximize(hola)

# Restricciones: 
constraints = [4*x + 6*y <= 120,
               2*x + 6*y <= 72,
               0*x + 1*y <= 10,
               x >= 0,
               y >= 0]

# Definir el problema de optimización
problem = cp.Problem(objective, constraints)

# Resolver el problema
problem.solve()

print("Resultado:")
print("Valor óptimo:", problem.value)
print("Valor de x:", x.value)
print("Valor de y:", y.value)
