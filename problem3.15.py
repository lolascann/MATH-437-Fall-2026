# Problem 3.15
import numpy as np
import matplotlib.pyplot as plt

#Part (a): Basic Feasible Solutions
basic_solutions = [
    (-4,0),
    (2,0),
    (-1,3)
]

print("Part (a): Basic Feasible Solutions")
for x1, x2 in basic_solutions:
    print(f"x1 = {x1}, x2 = {x2}, z = {x1 + 3*x2}")

# Part (b): Best Basic Solution
best_solution = max(basic_solutions, key=lambda p: p[0] + 3*p[1])
best_z = best_solution[0] + 3*best_solution[1]

print("Part (b): Best Basic Solution")
print("Optimal solution:", best_solution)
print("Maximum z:", best_z)

# Part (c): Graphical Solution
x1 = np.linspace(-5, 3, 400)

line1 = 2 - x1
line2 = 4 + x1

plt.figure(figsize=(9, 7))

plt.plot(x1, line1, label=r'$x_1 + x_2 = 2$')
plt.plot(x1, line2, label=r'$x_1 - x_2 = 4$')
plt.axhline(0, color="black", label=r'$x_2 = 0$')

# Feasible region vertices
vertices = np.array ([
    [-4,0],
    [2,0],
    [-1,3]
])

plt.fill(
    vertices[:, 0],
    vertices[:, 1],
    alpha=0.3,
    label="Feasible region"
)

for x, y in vertices:
    plt.scatter(x, y, color="green", zorder=5)
    plt.annotate( 
        f"({x}, {y})",
        (x, y),
        xytext=(6, 6),
        textcoords="offset points"
    )

# Optimal solution
plt.scatter(
    best_solution[0],
    best_solution[1],
    color="red",
    edgecolors="black",
    s=140,
    label="Optimal solution",
    zorder=6
)

plt.xlim(-5, 3)
plt.ylim(-1, 5),
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title("Problem 3.15")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()