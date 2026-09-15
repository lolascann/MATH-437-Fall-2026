import numpy as np
import itertools

#Variables:
#x1 = Model I
#x2 = Model II
#x3 = Model III

#Constraints:
A = np.array([
    [2, 3, 5],
    [4, 2, 7],
    [1, 0.5, 1/3],
    [2, -3, 0],
    [5, 0, -3]
])

b = np.array([
    4000,
    6000,
    1500,
    0,
    0
])

#Minimum production requirements:
minimum = np.array([200, 200, 150])

#Objective function:
c = np.array([30, 20, 50])

best_value = 0
best_solution = None

for t in np.linspace(100, 200, 100000):

    x1 = 3 * t
    x2 = 2 * t
    x3 = 5 * t

    solution = np.array([x1, x2, x3])

    #Check constraints:
    if 2*x1 + 3*x2 + 5*x3 <= 4000:
        if 4*x1 + 2*x2 + 7*x3 <= 6000:
            if x1 + 0.5*x2 + (1/3)*x3 <= 1500:
                if x1 >= 200 and x2 >= 200 and x3 >= 150:

                    value = np.dot(c, solution)

                    if value > best_value:
                        best_value = value
                        best_solution = solution

print("Optimal solution:")

print("Model I =", round(best_solution[0], 2))
print("Model II =", round(best_solution[1], 2))
print("Model III =", round(best_solution[2], 2))

print()
print("Maximum revenue = $", round(best_value, 2))