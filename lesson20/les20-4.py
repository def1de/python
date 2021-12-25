a = int(input('age: '))
if a < 2:
    print('Mladenec')
elif a>=2 and a<4:
    print('Malish')
elif a>=4 and a<13:
    print('Rebenok')
elif a>=13 and a<20:
    print('Podrostok')
elif a>=20 and a<65:
    print('Vzrosliy')
else:
    print('Pogiloy')
