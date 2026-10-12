# Problem 3.12
import numpy as np
from itertools import combinations

# Part (a): Maximize z
A_a = np.array([
    [1, 4, -2, 8, 1, 0],
    [-1, 2, 3, 4, 0, 1]
], dtype=float)

b_a = np.array([2, 1], dtype=float)
c_a = np.array([2, -4, 5, -6, 0, 0], dtype=float)

solutions_a = []

for basis in combinations(range(6), 2):
    B = A_a[:, basis]

    if abs(np.linalg.det(B)) < 1e-9:
        continue

    x = np.zeros(6)
    x[list(basis)] = np.linalg.solve(B, b_a)

    feasible = np.all(x >= -1e-9)
    z = np.dot(c_a, x)

    solutions_a.append((basis, x, feasible, z))

print("Part (a): Maximize z")
for basis, x, feasible, z in solutions_a:
    print(
        "Basis:", tuple(i + 1 for i in basis),
        "Solution:", np.round(x, 4),
        "Feasible:", feasible,
        "z:", round(z, 4)
    )

feasible_a = [s for s in solutions_a if s[2]]

if feasible_a:
    best_a = max(feasible_a, key=lambda s: s[3])
    print("\nOptimal solution (x1, x2, x3, x4):",
          np.round(best_a[1][:4], 4))
    print("Maximum z:", round(best_a[3], 4))


# Part (b): Minimize z
A_b = np.array([
    [1, 2, -3, 1],
    [1, 2, 1, 2]
], dtype=float)

b_b = np.array([4, 4], dtype=float)
c_b = np.array([1, 2, -3, -2], dtype=float)

solutions_b = []

for basis in combinations(range(4), 2):
    B = A_b[:, basis]

    if abs(np.linalg.det(B)) < 1e-9:
        continue

    x = np.zeros(4)
    x[list(basis)] = np.linalg.solve(B, b_b)

    feasible = np.all(x >= -1e-9)
    z = np.dot(c_b, x)

    solutions_b.append((basis, x, feasible, z))

print("\nPart (b): Minimize z")
for basis, x, feasible, z in solutions_b:
    print(
        "Basis:", tuple(i + 1 for i in basis),
        "Solution:", np.round(x, 4),
        "Feasible:", feasible,
        "z:", round(z, 4)
    )

feasible_b = [s for s in solutions_b if s[2]]

if feasible_b:
    best_b = min(feasible_b, key=lambda s: s[3])
    print("\nOptimal solution (x1, x2, x3, x4):",
          np.round(best_b[1], 4))
    print("Minimum z:", round(best_b[3], 4))
