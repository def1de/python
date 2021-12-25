city = {
    'London': 45,
    'Deli':68,
    'Kiev':47,
    'Krakow':50}
del(city['London'])
del(city['Deli'])
a = {k:city[k] for k, v in city.items()}
print(a)
