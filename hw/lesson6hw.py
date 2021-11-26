a=0
b=[2, 3, 4, 5, 6, 7, 8, 9]
for i in b:
    for y in b:
        a=i*y
        print(i,'*',y,'=',a)

input('Press ENTER')
c=int(input('Summa: '))
d=int(input('Procent: '))
e=int(input('Mesyac: '))
if e>12:
    k=e//12
    for x in range(k):
        c=c+c*(d/100)
        print(int(c))
else: print(int(c))
