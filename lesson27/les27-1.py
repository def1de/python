class Human:
    def __innit__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        self.now = 2021
    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCountry: {self.country}")

a=Human()
a.name='Illia'
a.age=14
a.country='UA'

a.info()
