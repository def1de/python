spisok_model = ['Машина', 'Робот','Айфон','Чехол']
spisok_usera = []
def pechat(a,b):
    while spisok_model:
        raspec = a.pop()
        b.append(raspec)
        print(b)
def gotovo(b):
    for i in b:
        print(f'{i} Ready')
pechat(spisok_model,spisok_usera)        
gotovo(spisok_usera)
