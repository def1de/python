import random
x=int(input('Stepen: '))
a=[random.randint(1, 10) for i in range(6)]
b=[random.randint(1, 10)**x for i in range(6)]
for i in a:
    for j in b:
        print(f"Я знаю твой ключ – {i}, его значение является {j}")
        break
