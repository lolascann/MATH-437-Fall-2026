# Fibonacci numbers
f0 = 1
f1 = 1

print("First 20 Fibonacci numbers:")

print(f0)
print(f1)

for n in range(2, 20):
    fn = f1 + f0
    print(fn)
    f0 = f1
    f1 = fn


# Lucas numbers
l0 = 2
l1 = 1

print("First 20 Lucas numbers:")

print(l0)
print(l1)

for n in range(2, 20):
    ln = l1 + l0
    print(ln)
    l0 = l1
    l1 = ln

    