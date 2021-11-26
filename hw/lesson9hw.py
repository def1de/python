print('NOTE: Type \'quit\' to quit.')
input('press ENTER to enter the main code')

print('\n#7.1')
while True:
    auto=str(input('What is your favorite auto?/nMy favorite auto is '))
    if auto == 'quit': break
    else:
        print(f'Let me see if I can find you a {auto}.\n')
input('Press ENTER')

print('\n#7.2')
while True:
    stol=str(input('How many places do you need?\nI need '))
    if stol != 'quit':
        stol=int(stol)       
        if stol<8:
            print('You offrered a place on tommorow.\n')
        else:
            print('You will need to wait a bit.\nWe will notice you when some plase will be free.\n')
    else: break
input('Press ENTER')

print('\n#7.3')
while True:
    num=str(input('Type your number '))
    if num == 'quit': break
    else:
        num=float(num)
        if num%10==0:
            print(f'The number {num} is a multiple of 10.\n')
        else:
            print(f'The number {num} is a unmultiple of 10.\n')
input('Press ENTER')

print('\n#7.4')
pizza=[]
while True:
    content = input('Enter ingridient: ')
    if content == 'quit':
        break
    elif content == 'ananas': #пасхалка
        print('I don\'t like ananas!') #ананас не добавляется в список ингредиентов
    else:
        pizza.append(content)
        content=''
print('Your ingridients:', ', '.join(pizza))
input('Press ENTER')

print('\n#7.5')
b=1
summa=0
while True:
    age=str(input(f'Enter the age of person #{b}: '))
    if age!='quit':
        age=int(age)
        if age<3: summa+=0
        elif age>12: summa+=15
        else: summa+=10
        b+=1
    else:
        break
print(f'\nVisit the cinema costs you {summa}USD')
input('Press ENTER')

print('\n#7.6')
pizza2=[]
active=0
while active<3: #active and while
    content2 = input('Enter ingridient: ')
    if content2 == 'quit':
        break
    else:
        pizza2.append(content2)
        content2=''
        active=len(pizza2) #active
print('Your ingridients:', ', '.join(pizza2))
input('Press ENTER')

print('\n#7.7')
while True:
    print('I <3 Python!')
