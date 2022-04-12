from entities.user import User
from db_connection import get_db


def get_user(result):
    if result:
        return User(result[1], result[2], result[3])
    else:
        return None


class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, user):
        cursor = self.db.cursor()

        cursor.execute(
            """INSERT INTO users (username, password, role) values (?, ?, ?)""",
            (user.username, user.password, user.role)
        )

        self.db.commit()

        return user

    def find_user(self, username):
        cursor = self.db.cursor()

        cursor.execute(
            """SELECT * FROM users WHERE username = ?""",
            (username,)
        )

        result = cursor.fetchone()

        return get_user(result)

    def get_id(self, username):
        cursor = self.db.cursor()

        cursor.execute(
            """SELECT id FROM users WHERE username = ?""",
            (username,)
        )

        result = cursor.fetchone()[0]
        return result


user_repository = UserRepository(get_db())
