def gen(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
        yield a

n=int(input("num: "))
t = gen(n)
print(f"0\n1")
for i in t:
    print(i)
