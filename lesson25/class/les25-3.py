class Human:
    def __init__(self, name, surname, age, pob, yob, now):
        self.name = name
        self.surname = surname
        self.age = age
        self.pob = pob
        self.yob = yob
        self.now = now

    def info(self):
        print(f"\nName: {self.name}\nSurname: {self.surname}\nPlace of birth: {self.pob}")

    def info1(self, now):
        year = self.yob
        age = now-year
        return age

p1=Human('Den', 'Dmitriev', 24, 'UA', 1997, 2021)
p1.info()
print(p1.info1(2021))
