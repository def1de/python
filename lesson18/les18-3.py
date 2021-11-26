import random
n=3
m=6
mat=[[random.randint(1, 9) for j in range(m)] for i in range(n)]
print(mat)
print("matrica ==>")
for i in mat:
    print(f"\t{i}")
