def fullName (name, surname):
    a=f'{name.title()} {surname.title()}'
    return a 

while True:
    print('Укажите имя и фамилию.')
    name=str(input('Имя: '))
    if name == 'break':
        break
    surname=str(input('Фамилия: '))
    if surname=='break':
        break
    b=fullName (name, surname)
    print(b)
print('Bye')
