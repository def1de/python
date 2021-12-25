import math

class Circle:
    def __init__(self, r):
        self.r = r

    def lenght(self):
        l=2*math.pi*self.r
        return l

    def size(self):
        s=math.pi*(self.r**2)
        return s

a1 = Circle(5)
print(a1.lenght())
print(a1.size())
print('='*18)

a2 = Circle(15)
print(a2.lenght())
print(a2.size())
print('='*18)

a3 = Circle(3.14)
print(a3.lenght())
print(a3.size())
print('='*18)
