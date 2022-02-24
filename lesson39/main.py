import sqlite3
from random import randint

bd = sqlite3.connect('user.db')
sql = bd.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT,
    cash INT
)""")
bd.commit()

def start():
    casino()
    enter()

def register():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM user WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user VALUES (?,?,?)", (user_login, user_password, 0))
        bd.commit()
        print('You registered\n')
    else:
        print('Already registered')
        for i in sql.execute("SELECT * FROM user"):
            print(i)
    casino()

def casino():
    user_login = input('Log in: ')
    number = randint(1, 2)
    sql.execute(f"SELECT login FROM user WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("Такого пользователя не существует!\nЗарегесрируйтесь")
        register()
    else:
        print('You succesfully logged in')
        if number == 1:
            print('You WON!')
            sql.execute(f"UPDATE user SET cash={1000} WHERE login = '{user_login}'")
            bd.commit()
        else:
            print('Lose')
            sql.execute(f"UPDATE user SET cash={0} WHERE login = '{user_login}'")
            bd.commit()

def enter():
    for values in sql.execute(f"SELECT login, cash FROM user"):
        print(values)

start()