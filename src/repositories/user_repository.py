from entities.user import User
from db_connection import get_db


def get_user(result):
    if result:
        return User(result[1], result[2], result[3])

    return None


class UserRepository:
    def __init__(self, db_):
        self.db_ = db_

    def create(self, user):
        cursor = self.db_.cursor()

        cursor.execute(
            """INSERT INTO users (username, password, role) values (?, ?, ?)""",
            (user.username, user.password, user.role)
        )

        self.db_.commit()

        return user

    def find_user(self, username):
        cursor = self.db_.cursor()

        cursor.execute(
            """SELECT * FROM users WHERE username = ?""",
            (username,)
        )

        result = cursor.fetchone()

        return get_user(result)

    def get_id(self, username):
        cursor = self.db_.cursor()

        cursor.execute(
            """SELECT id FROM users WHERE username = ?""",
            (username,)
        )

        result = cursor.fetchone()[0]
        return result

    def get_username(self, user_id):
        cursor = self.db_.cursor()

        cursor.execute(
            """SELECT username FROM users WHERE id = ?""",
            (user_id,)
        )

        result = cursor.fetchone()[0]
        return result

    def get_role(self, username):
        cursor = self.db_.cursor()

        cursor.execute(
            """SELECT role FROM users WHERE username = ?""",
            (username,)
        )

        result = cursor.fetchone()[0]
        return result


user_repository = UserRepository(get_db())
