import numpy as np
import matplotlib.pyplot as plt

def find_intersection(coeff1, const1, coeff2, const2):
    A = np.array([coeff1, coeff2])
    b = np.array([const1, const2])
    intersection = np.linalg.solve(A, b)
    return intersection

def plot_constraints_with_intersections(coefficients, rhs, labels, objective_coeff, objective_value, maximize=True):
    plt.figure(figsize=(10, 6))
    x = np.linspace(0, 50)  # Rango de valores para x
    colors = ['r', 'g', 'b', 'c', 'm', 'y']  # Colores para las restricciones

    for i in range(len(coefficients)):
        coef = coefficients[i]
        const = rhs[i]
        label = labels[i]
        y = (const - coef[0] * x) / coef[1]
        plt.plot(x, y, label=label, color=colors[i])

    intersections = []
    for i in range(len(coefficients)):
        for j in range(i + 1, len(coefficients)):
            intersection = find_intersection(coefficients[i], rhs[i], coefficients[j], rhs[j])
            intersections.append(intersection)

    intersections = np.array(intersections)
    plt.scatter(intersections[:, 0], intersections[:, 1], color='black', marker='o', label='Intersections')

    # Encuentra la dirección de la línea paralela
    if maximize:
        direction = objective_coeff
    else:
        direction = -objective_coeff
    
    # Encuentra el valor objetivo correspondiente a la línea paralela
    y_obj = (objective_value - direction[0] * x) / direction[1]
    plt.plot(x, y_obj, label='Objective Parallel', color='k', linestyle='--')

    plt.xlabel('Variable X1')
    plt.ylabel('Variable X2')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

def main():
    # Ejemplo de coeficientes de restricciones (ax + by <= c)
    coefficients = np.array([[4, 6],
                             [2, 6],
                             [0, 1]])
    rhs = np.array([120, 72, 10])  # Lado derecho de las restricciones
    labels = ['4*x + 6*y <= 120',
               '2*x + 6*y <= 72',
               '0*x + 1*y <= 10']

    objective_coeff = np.array([1, 1])  # Coeficientes de la función objetivo
    objective_value = 0  # Valor de la función objetivo

    plot_constraints_with_intersections(coefficients, rhs, labels, objective_coeff, objective_value)

if __name__ == '__main__':
    main()
