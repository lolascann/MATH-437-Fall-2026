# Problem 3.14
import numpy as np

# Part (a): Show both variables cannot be basic simultaneously
# Contraint matrix after substitution x2 = x2_plus - x2_minus
A = np.array([
    [-6, 7, -7, -9, -1],
    [1, 1, -1, 4, 0]
], dtype=float)

# Columns: x1, x2_plus, x2_minus, x3, surplus variable
x2_plus_column = A[:, 1]
x2_minus_column = A[:, 2]

print("Column for x2_plus:", x2_plus_column)
print("Column for x2_minus:", x2_minus_column)

#Check whether the columns are negative of each other
print("Are columns negatives?", np.allclose(x2_plus_column, -x2_minus_column))

# Check linear independence
B = A[:, [1, 2]]
print("Rank of these two columns:", np.linalg.matrix_rank(B))

if np.linalg.matrix_rank(B) < 2:
    print("The columns are linearly dependent.")
    print("Therefore, x2_pls and x2_minus cannot be basic")
