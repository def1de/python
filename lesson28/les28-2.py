class Mashin:
    def __innit__(self, mark, name, time, speed):
        self.mark = mark
        self.name = name
        self.time = time
        self.speed = speed
        print('Car detected')
class Rocket(Mashin):
    def info(self):
        print(f"Rocket: \n\t Mark{self.mark}\n\t Speed:{self.speed}")
class Boing(Mashin):
    def info_b(self):
        print(f"Rocket: \n\t Mark{self.mark}\n\t Speed:{self.speed}")

while True:
    n=int(input('1-space\n2-car\n3-Rocket\nEnter num: '))
    if n==1:
        
