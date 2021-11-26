auto=['audi', 'bmw', 'ferrari', 'ford', 'porshe']
print(auto)
message = f'Желаете ли вы купить {auto[0].title()}?'
print(message)
auto[2]='lambo'
print(auto)
auto.append('bugatti')
print(auto)
print(auto[5])
