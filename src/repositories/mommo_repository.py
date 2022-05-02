from entities.mommo import Mommo
from db_connection import get_db


def get_mommo(result):
    if result:
        return Mommo(result[1], result[2], result[3], result[4], result[5], result[6])

    return None


class MommoRepository:
    def __init__(self, db_):
        self.db_ = db_

    def create(self, mommo):
        cursor = self.db_.cursor()

        cursor.execute(
            """INSERT INTO mommo
            (user_id, name, hunger, thirst, clenliness, happiness)
            values (?, ?, ?, ?, ?, ?)""",
            (mommo.user_id, mommo.name, mommo.hunger,
             mommo.thirst, mommo.clenliness, mommo.happiness)
        )

        self.db_.commit()

        return mommo

    def get(self, user_id):
        cursor = self.db_.cursor()

        cursor.execute(
            """SELECT * FROM mommo WHERE user_id = ?""",
            (user_id,)
        )

        result = cursor.fetchone()

        return get_mommo(result)

    def get_all(self, user_id):
        cursor = self.db_.cursor()

        cursor.execute(
            """SELECT user_id, name FROM mommo WHERE user_id != ?""",
            (user_id,)
        )

        result = cursor.fetchall()

        return list(result)

    def save_mommo(self, mommo):
        cursor = self.db_.cursor()

        cursor.execute(
            """UPDATE mommo SET
            hunger = ?, thirst = ?, clenliness = ?, happiness = ? WHERE user_id = ?""",
            (mommo.hunger,
             mommo.thirst, mommo.clenliness, mommo.happiness, mommo.user_id)
        )

        self.db_.commit()


mommo_repository = MommoRepository(get_db())
