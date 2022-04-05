from db_connection import get_db

db = get_db()

db.execute("""INSERT INTO users
               (username, password, role) VALUES ('testi', 'testi', 0)""")

db.execute("""INSERT INTO mommo
               (user_id, name, hunger, thirst, clenliness, happiness) VALUES ('1', 'mommo', 100, 100, 100, 100)""")

db.commit()


result = db.execute("select * from users").fetchall()
print(result)

result = db.execute("select * from mommo").fetchall()
print(result)