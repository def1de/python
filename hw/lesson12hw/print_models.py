from printing_models import *

print('\n================================\n')
model_list=[]
a=''
i=1
while True:
    a=str(input(f'Enter {i} model: '))
    if a == 'quit':
        break
    else:
        model_list.append(a)
        i+=1
print('\n================================\n')
done_models(model_list)
print('\n================================\n')