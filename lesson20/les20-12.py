import random
m=int(input('m = '))
n=int(input('n = '))
k=int(input('k = '))
p=int(input('p = '))
r=int(input('r = '))
t=int(input('t = '))
a=[[random.randint(1, 9) for i in range(m)] for j in range(n)]
print("Matrica ==>")
for i in a:
    print(f"\t{i}")
for i in range(n):
    a[i][i]
print("Stroka ==>")
for i in range(m):
    print(f"\t{a[k][i]}")
print("Stolbec ==>")
for i in range(m):
    print(f"\t{a[i][p]}")
print("Diagonal ==>")
print (f"\t{b}")
print("Elem ==>")
print (f"\t{a[r][t]}")
