from entities.mommo import Mommo
from db_connection import get_db


def get_mommo(result):
    if result:
        return Mommo(result[1], result[2], result[3])

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

        return


mommo_repository = MommoRepository(get_db())
