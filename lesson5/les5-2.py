import math
a=float(input('a='))
print('x**2=', a)
if a>0:
    print('x=',math.sqrt(a),'/',math.sqrt(a)*-1)
elif a==0:
    print('x=',math.sqrt(a))
else:
    print('Error')
