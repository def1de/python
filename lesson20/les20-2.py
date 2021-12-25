import random
a = [random.randint(0, 15) for i in range(10)]
print(a)
print(f"First: {a[0]} Last: {a[-1]}")
s=1
for i in a:
    s*=i
print(f"Proizvedenie: {s}")
