# class User:
#     def __init__(self, first_name, last_name, age, country, attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.country = country
#         self.attempts = attempts
#     def describe_user(self):
#         print(f"{self.first_name.title()} {self.last_name.title()}, {self.age} years old, from {self.country}")
#     def greet_user(self):
#         print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
#     def login_attempts(self):
#         print(f'{self.attempts} login attempt(s)')
#     def increment_login_attempts(self):
#         self.attempts+=1
#     def restet_login_attempts(self):
#         self.attempts = 0

# class Admin(User):
#     def __init__(self, first_name, last_name, age, country, attempts):
#         super().__init__(first_name, last_name, age, country, attempts)
#         self.priveleges = ['Allowed to add messages', 'Allowed to delete users', 'Allowed to ban users']
#     def show_priveleges(self):
#         for i in self.priveleges:
#             print (i)

# class Privileges(Admin):
#     def __init__(self, first_name, last_name, age, country, attempts):
#         super().__init__(first_name, last_name, age, country, attempts)
#         super().show_priveleges()
#     def show_priveleges(self):
#         for i in self.priveleges:
#             print (i)

from user_class import *
from other_class import *

user1 = User('Illia', 'Katerynych', 14, 'Ukraine', 0)
user1.describe_user()
user1.greet_user()
user1.login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.login_attempts()
user1.restet_login_attempts()
user1.login_attempts()

print('\n')

admin = Admin('Illia', 'Katerynych', 14, 'Ukraine', 0)
admin.show_priveleges()

print('\n')

priv = Privileges('Illia', 'Katerynych', 14, 'Ukraine', 0)