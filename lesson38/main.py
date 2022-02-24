import sqlite3

bd = sqlite3.connect('user.db')
sql = bd.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT,
    cash INT
)""")
bd.commit()

user_login = input('Login: ')
user_password = input('Password: ')

sql.execute(f"SELECT login FROM user WHERE login = '{user_login}'" )
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO user VALUES (?,?,?)", (user_login, user_password, 0))
    bd.commit()
    print('registered')
else:
    print('Already registered')

for i in sql.execute("SELECT * FROM user"):
    print(i)