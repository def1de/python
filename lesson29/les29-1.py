class Car:
    def __init__(self, mark, model, city, adometr):
        self.mark = mark
        self.model = model
        self.city = city
        self.addometr=0
        self.adometr=adometr
        
    def info(self):
        print(f"Mark: {self.mark}\nModel: {self.model}\nCity: {self.city}")
        
    def readAdometr(self):
        print(f"Probeg: {self.adometr} km")
        
    def updateAdometr(self, n):
        if self.adometr<n:
            print('\nDon\'t cheat!\nF@cking scemmer')
        else:
            self.adometr=n
            print(f"\nUpdated probeg: {self.adometr} km")
        
        
    def addAdometr(self, added):
        if self.adometr>self.adometr+added:
            print('\nDon\'t cheat!\nF@cking scemmer')
        else:
            self.adometr=n
            print(f"\nUpdated probeg: {self.adometr} km")
            self.adometr += added
            print('\nprobeg updated')
            print(f"Updated probeg: {self.adometr} km")

class ECar(Car):
    def __init__(self, mark, model, city, adometr, battery):
        super().__init__(mark, model, city, adometr)
        self.battery = battery
        
    def info_battery(self):
        print(f"{self.battery} mAh")
    

a = Car('Kia', 'K5', 'Kr', 25)
n=int(input('update adometr: '))
added=int(input('Increment adometr: '))

a.info()
a.readAdometr()
a.updateAdometr(n)
a.addAdometr(added)

b = ECar('Kia', 'K5', 'Kr', 23, 5000)
b.info_battery()
