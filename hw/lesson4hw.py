print('#3.7')
guests=['mama', 'papa', 'napoleon']
messege1 = f'Приглашаем вас на обед, {guests[0].title()}.'
messege2 = f'Приглашаем вас на обед, {guests[1].title()}.'
messege3 = f'Приглашаем вас на обед, {guests[2].title()}.'
print(messege1)
print(messege2)
print(messege3)
del_name=guests.pop(2)
print(del_name + ' не пришёл :(')
guests.insert(0, 'dedushka')
guests.insert(2, 'pradeduska')
guests.append('babuska')
messege4 = f'Приглашаем вас на обед, {guests[0].title()}.'
messege5 = f'Приглашаем вас на обед, {guests[1].title()}.'
messege6 = f'Приглашаем вас на обед, {guests[2].title()}.'
messege7 = f'Приглашаем вас на обед, {guests[3].title()}.'
messege8 = f'Приглашаем вас на обед, {guests[4].title()}.'
print(guests)
print(messege4)
print(messege5)
print(messege6)
print(messege7)
print(messege8)
nep1=guests.pop(0)
nep2=guests.pop(1)
nep3=guests.pop(2)
print('Сожалеем, '+nep1)
print('Сожалеем, '+nep2)
print('Сожалеем, '+nep3)
messege9 = f'Приглашаем вас на обед, {guests[0].title()}.'
messege10 = f'Приглашаем вас на обед, {guests[1].title()}.'
print(messege9)
print(messege10)
print('Всего: ')
print(len(guests))

input('\nEnd of 3.7\npress ENTER\n')

print('#3.8')
strani = ['Germany', 'Austria', 'UK', 'USA', 'Canada']
print('sorted by sorted(list):')
print(sorted(strani)) #sorted
print('default')
print(strani) #default
print('reversed:')
strani.reverse()
print(strani) #reverse
print('default')
strani.reverse()
print(strani) #default
print('sorted by list.sort():')
strani.sort()
print(strani) #sorted
print('reversed and sorted:')
strani.sort(reverse=1)
print(strani) #default

input('\nEnd of 3.8\npress ENTER\n')

print('#3.10')
list=['1', '5', '4', '3', '2']
print (list)
messege11 = f'Вам нраится число {list[0]}.'
print(messege11)
deleted=list.pop(1)
print('Число '+deleted+' пропало\n')
print('deleted 4th elem of list:')
del list[3]
print (list)
print('sorted by sorted(list):')
print(sorted(list)) #sorted
print(list) #default
print('reversed:')
list.reverse()
print(list) #reverse
list.reverse()
print('sorted by list.sort():')
list.sort()
print(list) #sorted
print('reversed and sorted:')
list.sort(reverse=1)
print(list) #reversed and sorted

input('\nEnd of 3.10\npress ENTER\n')
