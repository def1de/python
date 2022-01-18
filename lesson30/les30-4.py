class Bank:
    def __init__(self, purse, depos_amount, withdraw_amount):
        self.purse = purse
        self.depos_amount = depos_amount
        self.withdraw_amount = withdraw_amount
    def show_purse(self):
        print(f"Your purse is >>> {self.purse}")
    def deposit(self):
        self.purse+=self.depos_amount
        print(f"Your purse is >>> {self.purse}")
    def withdraw(self):
        self.purse-=self.withdraw_amount
        print(f"Your purse is >>> {self.purse}")


def menu():
    print(f"\n1 - show purse\n2 - deposit\n3 - withdraw\n")

user = Bank(0, 0, 0)
while True:
    menu()
    choise = int(input('Your choise >>> '))
    print('\n')
    if choise == 1:
        user.show_purse()
    elif choise == 2:
        user.depos_amount = int(input('Deposit Amount >>> '))
        user.deposit()
    elif choise == 3:
        user.withdraw_amount = int(input('Withdraw Amount >>> '))
        user.withdraw()
    else:
        print('Error!')