class Human:
    def info(self, n):
        for i in range(n):
            print(f"\nName: {self.name}\nSurname: {self.surname}\nPlace of birth: {self.place_of_birth}")
    def info1(self, now):
        year = self.year_of_birth
        age = now-year
        return age
    pass
p1=Human()
p1.name = 'Den'
p1.surname = 'Dmitriev'
p1.place_of_birth = 'UA'
p1.year_of_birth = 1997

p1.info(1)
print(p1.info1(2021), 'Years')

p2=Human()
p2.name = 'Stas'
p2.surname = 'Matveychuk'
p2.place_of_birth = 'UA'
p2.year_of_birth = 2006

p2.info(1)
print(p2.info1(2021), 'Years')

p3=Human()
p3.name = 'Illia'
p3.surname = 'Katerynych'
p3.place_of_birth = 'UA'
p3.year_of_birth = 2007

p3.info(1)
print(p3.info1(2021), 'Years')
