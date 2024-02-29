import numpy as np
import random

n = 5
capacity = 30
objects_values = [7, 3, 2, 6, 9]
objects_weight = [12, 16, 11, 10, 18]

def generate_initial_solutions(n):
    solutions = [random.randint(0, 1) for _ in range(n)]
    weight = total_weight(objects_weight, solutions)
    while weight > capacity:
        solutions = generate_initial_solutions(n)
        weight = total_weight(objects_weight, solutions)
    return solutions
      
def total_values(objects_values, solutions):
    return sum(objects_values[i] * solutions[i] for i in range(len(solutions)))

def total_weight(objects_weight, solutions):
    return sum(objects_weight[i] * solutions[i] for i in range(len(solutions)))

solutions_initiales = generate_initial_solutions(n)
values = total_values(objects_values, solutions_initiales)
weight = total_weight(objects_weight, solutions_initiales)

print("\n---------------------------------------\n")
print("\n---- Solutions initiales  ----\n")
print("Initial solution : {}".format(solutions_initiales))
print("Valeur initiale: {}".format(values))
print("Poids inital: {}".format(weight))

solutions_initiales = generate_initial_solutions(n)

def hill_climbing(objects_values, objects_weight, capacity, n, solutions_initiales):
    solutions = solutions_initiales
    values = total_values(objects_values, solutions)
    weight = total_weight(objects_weight, solutions)
    

    for _ in range(100):
        neighbors = []
        neighbor = solutions
        for i in range(n):
            neighbor[i] = 1 - neighbor[i]
            neighbors.append(neighbor)
            
    best_neighbor = max(neighbors, key = lambda x: total_values(objects_values, x) if total_weight(objects_weight, x) <= capacity else -1)
    best_neighbor_value = total_values(objects_values, best_neighbor)
    best_neighbor_weight = total_weight(objects_weight, best_neighbor)
    
    if best_neighbor_value > values and best_neighbor_weight <= capacity:
        solutions = best_neighbor
        values = best_neighbor_value
        weight = best_neighbor_weight
        
    return solutions, values, weight

def perturbation(x):
    random.shuffle(x)

def recherhe_locale_iteree(objects_values, objects_weight, capacity, n, x0):
    x, values, weight = hill_climbing(objects_values, objects_weight, capacity, n, x0)
    
    for _ in range(100):
        x1 = [k for k in x]
        perturbation(x1)
        x2, values2, weight2 = hill_climbing(objects_values, objects_weight, capacity, n, x1)

        if values2 > values:
            x, values, weight = x2, values2, weight2

    return x, values, weight

solutions_hill, values_hill, weights_hill = hill_climbing(objects_values, objects_weight, capacity, n, solutions_initiales) 

print("\n---------------------------------------\n")
print("\n---- Recherce Locale (Hill Climbing)  ----\n")
print("Optimal solution : {}".format(solutions_hill))
print(" Values : {}".format(values_hill))
print(" Weights : {}".format(weights_hill))

solutions_rli, values_rli, weights_rli = recherhe_locale_iteree(objects_values, objects_weight, capacity, n, solutions_initiales) 

print("\n---------------------------------------\n")
print("\n---- Recherce Locale Iteree  ----\n")
print("Optimal solution  : {}".format(solutions_rli))
print(" Values : {}".format(values_rli))
print(" Weights : {}".format(weights_rli))