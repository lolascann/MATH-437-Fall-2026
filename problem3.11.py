# Problem 3.11
import numpy as np
import matplotlib.pyplot as plt

# Part (a): Equation Form
# x1 + 3x2 + x3 = 6
# 3x1 + 2x2 + x4 = 6

# Part (b): Basic Solutions
# (6/7, 12/7, 0, 0) - Feasible
# (2, 0, 4, 0) - Feasible
# (6, 0, 0, -12) - Infeasible
# (0, 3, -3, 0) - Infeasible
# (0, 2, 0, 2) - Feasible
# (0, 0, 6, 6) - Feasible

# Part (c): Optimal Basic Feasible Solution
optimal_x1 = 6 / 7
optimal_x2 = 12 / 7
optimal_z = 2 * optimal_x1 + 3 * optimal_x2

print("Optimal solution:", (optimal_x1, optimal_x2))
print("Maximum z:", optimal_z)

# Part (d): Graphical Verification
x1 = np.linspace(0, 6, 400)
line1 = (6 - x1) / 3
line2 = (6 - 3 * x1) / 2

plt.figure(figsize=(9, 7))
plt.plot(x1, line1, label=r'$x_1 + 3x_2 = 6$')
plt.plot(x1, line2, label=r'$3x_1 + 2x_2 = 6$')

vertices = np.array([
    [0, 0],
    [2, 0],
    [6 / 7, 12 / 7],
    [0, 2]
])

plt.fill(vertices[:, 0], vertices[:, 1],
         alpha=0.3, label="Feasible region")

for x, y in vertices:
    plt.scatter(x, y, color="green")
    plt.annotate(f"({x:.2f}, {y:.2f})", (x, y),
                 xytext=(5, 5), textcoords="offset points")

plt.scatter(optimal_x1, optimal_x2, color="gold",
            edgecolors="black", s=140, label="Optimal solution")

# Part (e): Infeasible Basic Solutions
infeasible_points = [(6, 0), (0, 3)]

for x, y in infeasible_points:
    plt.scatter(x, y, color="red", marker="x", s=100)
    plt.annotate(f"({x}, {y}) infeasible", (x, y),
                 xytext=(5, 5), textcoords="offset points",
                 color="red")

plt.xlim(-0.5, 6.8)
plt.ylim(-0.5, 3.5)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title("Problem 3-11: Linear Programming")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
