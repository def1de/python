a=float(input('a='))
x=float(input('x='))
if x>0:
    if a>=0:
        y=a*x
    else:
        y=2*a*x
else:
    y=2
print('y=',y)
