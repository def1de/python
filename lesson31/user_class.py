class User:
    def __init__(self, first_name, last_name, age, country, attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.attempts = attempts
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, {self.age} years old, from {self.country}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
    def login_attempts(self):
        print(f'{self.attempts} login attempt(s)')
    def increment_login_attempts(self):
        self.attempts+=1
    def restet_login_attempts(self):
        self.attempts = 0