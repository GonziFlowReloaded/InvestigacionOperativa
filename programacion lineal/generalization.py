import cvxpy as cp


arreglo = []
for i in range(2):
    arreglo.append(cp.Variable())

def funcion_Maximizar(x, multiplicador, restricciones):
    for i in range(len(x)):
        funcion = multiplicador[i] * x[i]
    objetivo = cp.Maximize(funcion)

    resultados = []
    
        
    resultados.append(cp.Problem(objetivo, restricciones).solve())
    for i in range(len(x)):
        resultados.append(float(x[i].value))
    return resultados



multiplicador = [2, 4]
constraints = [4*arreglo[0] + 6*arreglo[1] <= 120,
               2*arreglo[0] + 6*arreglo[1] <= 72,
               0*arreglo[0] + 1*arreglo[1] <= 10,
               arreglo[0] >= 0,
               arreglo[1] >= 0]

print(funcion_Maximizar(arreglo, multiplicador, constraints))

