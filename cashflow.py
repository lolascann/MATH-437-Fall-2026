import numpy as np
import itertools

# Variables:
# x1 = Project 1
# x2 = Project 2
# x3 = Project 3
# x4 = Project 4
# b1 = Bank after Year 1
# b2 = Bank after Year 2
# b3 = Bank after Year 3
# b4 = Bank after Year 4

#Constraints:
A = np.array([
   [1, 1, 0, 1, 1, 0, 0, 0],
    [0.50, 0.60, -1, 0.40, 1.065, -1, 0, 0],
    [0.30, 0.20, 0.80, 0.60, 0, 1.065, -1, 0],
    [1.80, 1.50, 1.90, 1.80, 0, 0, 1.065, -1]])

b = np.array([10,0,0,0])

#Objective function:
c = np.array([1.20,1.30,0.80,0.95,0,0,0,1.065])

best_value = 0
best_solution = None

#Check all possible combinations of 4 variables
for variables in itertools.combinations(range(8), 4):

    matrix = A[:, variables]

    # Skip if the matrix cannot be solved
    if abs(np.linalg.det(matrix)) < 0.000001:
        continue

    solution = np.zeros(8)

    solution[list(variables)] = np.linalg.solve(matrix, b)

    if np.all(solution >= 0):

        value = np.dot(c, solution)

        if value > best_value:
            best_value = value
            best_solution = solution

#Print answer:
names = [
    "Project 1",
    "Project 2",
    "Project 3",
    "Project 4",
    "Bank Year 1",
    "Bank Year 2",
    "Bank Year 3",
    "Bank Year 4"
]

print("Optimal solution:")

for name, value in zip(names, best_solution):
    print(name, "=", round(value, 3), "thousand dollars")

print()
print("Maximum value =", round(best_value, 3), "thousand dollars")
print("Maximum value = $", round(best_value * 1000, 2))

