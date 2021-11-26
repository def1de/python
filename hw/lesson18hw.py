import random
m=5
n=5
b=[]
a=[[random.randint(1, 9) for i in range(m)] for j in range(n)]
print("Matrica ==>")
for i in a:
    print(f"\t{i}")
print("Diagonal ==>")
for i in range(n):
    b.append(a[i][i])
print (f"\t{b}")
print("Random ==>")
print (f"\t{a[random.randint(0, m)][random.randint(0, n)]}")
