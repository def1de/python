import math

x=float(input('Enter x: '))
if x >=0 and x < 2:
    y=x*(math.sqrt(x-5.4))
elif x >= 2 and x<8:
    y=math.atan(x**2)
elif x>=8:
    y=math.log(abs(x-7.8))
else:
    print('Error!')
print(f"y = {y}")
