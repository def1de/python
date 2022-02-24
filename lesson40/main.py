import random

def task1(name):
    print(f"Hello {name}")

def task2(par, n):
    print((par + ' ') * n)

def task6(a, b):
    if a>b:
        print(a)
    elif a < b:
        print(b)
    elif a == b: print('equal (=)')
    else: print("error")

def task7(a, b, c):
    transfer = a
    if transfer < b: transfer = b
    if transfer < c: transfer = c
    return transfer

def task8(a, b, c):
    transfer = task7(side_a, side_b, side_c)
    if transfer == a:
        if b+c > a:
            print('True')
        else: print('False')
    elif transfer == b:
        if a+c > b:
            print('True')
        else: print('False')
    elif transfer == c:
        if a+b > c:
            print('True')
        else: print('False')
    else: print(equal)

def task9(a, b):
    print(f"{a}{b}")

def task10(a, b, c):
    if c == '+': return a+b
    elif c == '-': return a-b
    elif c == '*': return a*b
    elif c == '/': return a/b
    else: print('Error')

def task11(tag, text):
    print(f"<{tag}>{text}</{tag}>")

def task12(month):
    if month == 12 or month == 1 or month == 2:
        print('Winter')
    elif month == 3 or month == 4 or month == 5:
        print('Spring')
    elif month == 6 or month == 7 or month == 8:
        print('Summer')
    elif month == 9 or month == 10 or month == 11:
        print('Autumn')
    else: print('Error!')

def task13(arr):
    for i in arr:
        print('*' * i)

def task14(a):
    if a%2 == 0: print('True')
    else: print('False')

def task15(arr):
    arr1 = []
    transfer = arr[0]
    arr1.append(transfer)
    transfer = arr[-1]
    arr1.append(transfer)
    print(arr1)

def task16(n):
    f=1
    for i in range(1, n):
        f*=i
    return f

# name = str(input('Your name: '))
# task1(name)

# par = str(input('Ryadok: '))
# par_n = int(input('Mnojitel: '))
# task2(par, par_n)

# num1 = int(input('num1: '))
# num2 = int(input('num2: '))
# task6(num1, num2)

# num_a = int(input('num1: '))
# num_b = int(input('num2: '))
# num_c = int(input('num3: '))
# print(task7(num_a, num_b, num_c))

# side_a = int(input('num1: '))
# side_b = int(input('num2: '))
# side_c = int(input('num3: '))
# task8(side_a, side_b, side_c)

# str_1 = str(input('str1: '))
# str_2 = str(input('str2: '))
# task9(str_1, str_2)

# num_a = float(input('num1: '))
# num_b = float(input('num2: '))
# num_c = str(input('+/-/*//: '))
# print(task10(num_a, num_b, num_c))

# str_1 = str(input('str1: '))
# str_2 = str(input('str2: '))

# sometext = str(input('str: '))
# tag = str(input('tag: '))
# task11(tag, sometext)

# month = int(input('Month: '))
# task12(month)

# arr = [random.randint(1, 10) for i in range(1, 10)]
# task13(arr)

# is_2 = int(input('Num: '))
# task14(is_2)

# arr = [random.randint(1, 10) for i in range(1, 10)]
# task15(arr)
#
# num = int(input())
# print(task16(num))

