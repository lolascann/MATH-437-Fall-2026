import numpy as np

#Demand:
A_demand = np.array([500, 5000, 750])
B_demand = np.array([1000, 1200, 1200])

#Production rates:
A_rate = 0.75
B_rate = 1

#Monthly capacity:
capacity = np.array([3000, 3500, 3000])

#Total hours needed:
A_hours = np.sum(A_demand) / A_rate
B_hours = np.sum(B_demand) / B_rate

#otal hours available:
total_capacity = np.sum(capacity)

print("Hours needed for A =", A_hours)
print("Hours needed for B =", B_hours)

print("Total hours needed =", A_hours + B_hours)
print("Total hours available =", total_capacity)

if A_hours + B_hours <= total_capacity:
    print("The problem is feasible.")
else:
    print("The problem is NOT feasible.")
