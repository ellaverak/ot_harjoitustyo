from entities.mommo import Mommo
from db_connection import get_db


def get_mommo(result):
    """luo tietokantatietojen perusteella Mommo-olion.

    Args:
        result (lista): mömmön tietokantatiedot.

    Returns:
        Mommo: Mommo-olio.
    """

    if result:
        return Mommo(result[1], result[2], result[3], result[4], result[5], result[6])

    return None


class MommoRepository:
    def __init__(self, db_):
        """luokan konstruktori, joka luo uuden mömmön talletustoiminnoista vastaavan palvelun.

        Args:
            db_ (yhteys): tietokantayhteys.
        """

        self.db_ = db_

    def create(self, mommo):
        """tallentaa uuden mömmön tietokantaan.

        Args:
            mommo (Mommo): Mommo-olio.

        Returns:
            Mommo: tallennettu Mommo-olio.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            """INSERT INTO mommo
            (user_id, name, hunger, thirst, clenliness, happiness)
            values (?, ?, ?, ?, ?, ?)""",
            (mommo.user_id, mommo.name, mommo.hunger,
             mommo.thirst, mommo.clenliness, mommo.happiness)
        )

        cursor.execute(
            "SELECT id FROM mommo WHERE user_id = ?",
            (mommo.user_id,)
        )

        result = cursor.fetchone()[0]

        cursor.execute(
            """INSERT INTO tricks
            (mommo_id, jump, squish, play_dead)
            values (?, ?, ?, ?)""",
            (result, 0, 0, 0)
        )

        self.db_.commit()

        return mommo

    def get(self, user_id):
        """hakee mömmön tietokannasta käyttäjän id tunnuksen perusteella.

        Args:
            user_id (int): käyttäjän id-tunnus.

        Returns:
            Mommo: haettu mömmö Mommo-oliona.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT * FROM mommo WHERE user_id = ?",
            (user_id,)
        )

        result = cursor.fetchone()

        return get_mommo(result)

    def get_all(self, user_id):
        """hakee kaikki mömmöt tietokannasta, paitsi nykyisen käyttäjän mömmön.

        Args:
            user_id (int): nykyisen käyttäjän id-tunnus.

        Returns:
            lista: kaikki kaikki mömmöt listana [user_id, mommo].
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT user_id, name FROM mommo WHERE user_id != ?",
            (user_id,)
        )

        result = cursor.fetchall()

        return list(result)

    def save_mommo(self, mommo):
        """tallentaa nykyisen mömmön tietokantaan.

        Args:
            mommo (Mommo): Mommo-olio.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            """UPDATE mommo SET
            hunger = ?, thirst = ?, clenliness = ?, happiness = ? WHERE user_id = ?""",
            (mommo.hunger,
             mommo.thirst, mommo.clenliness, mommo.happiness, mommo.user_id)
        )

        self.db_.commit()

    def get_trick(self, mommo_id):
        """hakee mömmän temput tietokannasta.

        Args:
            mommo_id (int): mömmön id-tunnus.

        Returns:
            lista: temput listana.
        """
        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT jump, squish, play_dead FROM tricks WHERE mommo_id = ?",
            (mommo_id,)
        )

        result = cursor.fetchall()[0]

        return list(result)

    def get_id(self, user_id):
        """hakee mömmön id-tunnuksen tietokannasta käyttäjän id-tunnuksen perusteella.

        Args:
            user_id (int): käyttäjän id-tunnus.

        Returns:
            int: mömmön id-tunnus.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT id FROM mommo WHERE user_id = ?",
            (user_id,)
        )

        result = cursor.fetchone()[0]
        return result

    def save_trick(self, mommo_id, trick_list):
        """tallentaa temput tietokantaan.

        Args:
            mommo_id (int): mömmön id-tunnus.
            trick_list (lista): temput listana.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            """UPDATE tricks SET
            jump = ?, squish = ?, play_dead = ? WHERE mommo_id = ?""",
            (trick_list[0], trick_list[1], trick_list[2], mommo_id)
        )

        self.db_.commit()


mommo_repository = MommoRepository(get_db())
