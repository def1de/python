from user_class import User

class Admin(User):
    def __init__(self, first_name, last_name, age, country, attempts):
        super().__init__(first_name, last_name, age, country, attempts)
        self.priveleges = ['Allowed to add messages', 'Allowed to delete users', 'Allowed to ban users']
    def show_priveleges(self):
        for i in self.priveleges:
            print (i)

class Privileges(Admin):
    def __init__(self, first_name, last_name, age, country, attempts):
        super().__init__(first_name, last_name, age, country, attempts)
        super().show_priveleges()
    def show_priveleges(self):
        for i in self.priveleges:
            print (i)