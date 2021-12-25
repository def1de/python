import random
n = int(input('n = '))
print(list(filter(lambda x:x%2==0, [random.randint(0, 10) for i in range(n)])))
