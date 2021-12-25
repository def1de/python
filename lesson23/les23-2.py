def gen(n):
    yield n
    print ("1й пребор")
    yield n+1
    print ("2й пребор")
    yield n*3
    print ("3й пребор")
    yield ""
n=int(input("num: "))
t = gen(n)
for i in t:
    print(i)
