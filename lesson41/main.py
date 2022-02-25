import math
import random

#1
radius = int(input('radius: '))
SorL = input('S if you want to find space/nOr L if you want to find lenght\n>>> ')
if SorL == 'S':
    print(math.pi*radius**2)
elif SorL == 'L':
    print(2*math.pi*radius)
else: print('Error!')

#2
password = str(input('password: '))
confirm_password = str(input('Confirm password: '))
if confirm_password == password: print('Correct')
else: print('Wrong!')

#3
age = int(input('Age: '))
if age >= 18:
    stependia = int(input('Stependia: '))
    if stependia >= 1000:
        print('You can affort a credit')
    else:
        print('You can\'t afford a credit')
else:
    print('You can\'t afford a credit')

#4
i = 1
n=1
s=0
while n != 0:
    n = int(input(f'Grade #{i}: '))
    s+=n
    i+=1
i-=1
print(s/i)

#5
x = int(input('x = '))
y = int(input('y = '))
if x>y: print(math.sqrt(x*y))
else: print(math.log(x+y))

#6
i=0
while i!=10: #проверяет только 10 раз ибо бесконечный цикл не есть гуд
    t = random.randint(0, 40)
    if t >= 20: print('Switched on')
    else: print('Switched off')
    i+=1

#7
num=int(input('Ur num: '))
if num%2 == 0: print('2nd')
else: print('1st')

#8
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
max_l = max(a, b, c)
if max_l == a:
    if b+c>a: print(True)
    else: print(False)
elif max_l == b:
    if a+c>b: print(True)
    else: print(False)
elif max_l == c:
    if a+b>c: print(True)
    else: print(False)
else: print(False)

#9
x_coord = int(input('x = '))
y_coord = int(input('y = '))
if x_coord>0 and y_coord>0: print('1st 1/4')
elif x_coord<0 and y_coord>0: print('2st 1/4')
elif x_coord<0 and y_coord<0: print('3st 1/4')
elif x_coord>0 and y_coord<0: print('4st 1/4')
else: print(False)

#10
x1 = int(input('x='))
if x1>0: y1=2*x1-10
elif x1==0: y1=0
elif x1<0: y1=2*abs(x1)-1
else: print(False)
print(f'y={y1}')