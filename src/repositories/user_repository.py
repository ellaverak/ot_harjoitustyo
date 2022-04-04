#from entities.user import User
from db_connection import get_db

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

user_repository = UserRepository(get_db())