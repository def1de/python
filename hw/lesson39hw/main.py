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
    sql.execute(f"SELECT login FROM user WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("Такого пользователя не существует!\nЗарегесрируйтесь")
        register()
    else:
        print('You succesfully logged in')
        while True:
            start_btn = str(input('1. Press ENTER to play\n2. Type CASH to check ballance\n3. Type QUIT to quit\n>>> '))
            if start_btn == '':
                number = randint(1, 2)
                if number == 1:
                    print('\n===================\nYou WON! o(*^＠^*)o\n===================\n')
                    sql.execute(f"UPDATE user SET cash=cash+1000 WHERE login = '{user_login}'")
                    bd.commit()
                else:
                    print('\n====================\nYou Lose! `(*>﹏<*)′\n====================\n')
                    sql.execute(f"UPDATE user SET cash={0} WHERE login = '{user_login}'")
                    bd.commit()
            elif start_btn == 'cash' or 'CASH':
                sql.execute(f"SELECT cash FROM user WHERE login = '{user_login}'")
                print(sql.fetchone())
            elif start_btn == 'quit' or 'QUIT':
                break
            else: print('Error! Command not found. Try again...')

casino()