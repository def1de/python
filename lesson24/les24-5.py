def even_n(i):
    if i%2==0:
        return True
    else:
        return False

a=[i for i in range(1000001)]
f=list(filter(even_n, a))
print(f)
