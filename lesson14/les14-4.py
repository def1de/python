dictName={'Illia':18, 'Maksym':20, 'Den':24, 'Roma':7}
dictAuto={'Kia_K5': 2014, 'Toyota_Supra': 2000, 'BMW_M2': 2016, 'Volkswagen_Tiguan': 2020}
dictMixed = dictName.copy()
dictMixed.update(dictAuto)
dictMixed=dictName | dictAuto
dictName|=dictAuto
print (dictName)
a=dictName.get('Maksym', 'user_not_found')
dictAuto.clear()
print(a)
print(dictAuto)