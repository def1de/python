class Animal:
    def __init__(self):
        self.species = 'ordinary'
        self.sound = 'Grrr!'
    def info(self):
        if self.species=='ordinary':
            print(f"I'm an {self.species} animal\n{self.sound} {self.sound}")
        else:
            print(f"{self.species.title()} is not animal.")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.species = 'dog'
        self.sound = 'Woof!'
    def info(self):
        if self.species=='dog':
            print(f"I'm an {self.species} animal\n{self.sound} {self.sound}")
        else:
            print(f"{self.species.title()} is not animal.")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.species = 'cat'
        self.sound = 'Meow!'
    def info(self):
        if self.species=='cat':
            print(f"I'm an {self.species} animal\n{self.sound} {self.sound}")
        else:
            print(f"{self.species.title()} is not animal.")

print('\n')
a = Animal()
a.info()

print('\n')

d = Dog()
d.info()

print('\n')

c = Cat()
c.info()

print('\n')