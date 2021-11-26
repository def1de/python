#7.1
c=input("What kind of car do you want?")
print(f"Let me see if I can find you a {c}")

#7.2
a=int(input("На скольких людей вы бронируете столик?"))
if a>8:
    print("Вам придется подождать")
else:
    print("Ваш столик готов")

#7.3
b=int(input("Введите число"))
if b//10:
    print("Число кратное 10")
else:
    print("Число не кратное 10")

#7.4,7.6
active=True
while active:
    d=input("Какуе добавление вы желаете для вашей пиццы?(Для отмены напишите 'quite'")
    if d=="quite":
        print("Ваша пицца готовиться")
        active= False
    else:
        print(f"{d} Добавлена в вашу пиццу")

#7.5
age=int(input("Введите ваш возраст"))
if age<3:
    print("Билет бесплатный")
elif age>=3 and age<=12:
    print("Билет стоит 10$")
else:
    print("Билет стоит 15$")
#7.7
k=2
while k>1:
    k+=1
    print(k)