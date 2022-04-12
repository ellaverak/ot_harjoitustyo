from db_connection import get_db

db = get_db()

result = db.execute("select * from users").fetchall()
print(result)

result = db.execute("select * from mommo").fetchall()
print(result)
