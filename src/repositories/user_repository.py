from entities.user import User
from db_connection import get_db


def get_user(result):
    """luo tietokantatietojen perusteella User-olion.

    Args:
        result (lista): käyttäjän tietokantatiedot.

    Returns:
        User: User-olio.
    """

    if result:
        return User(result[1], result[2], result[3])

    return None


class UserRepository:
    def __init__(self, db_):
        """luokan konstruktori, joka luo uuden käyttäjän talletustoiminnoista vastaavan palvelun.

        Args:
            db_ (yhteys): tietokantayhteys.
        """

        self.db_ = db_

    def create(self, user):
        """tallentaa uuden käyttäjän tietokantaan.

        Args:
            user (User): User-olio.

        Returns:
            User: tallennettu User-olio.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "INSERT INTO users (username, password, role) values (?, ?, ?)",
            (user.username, user.password, user.role)
        )

        self.db_.commit()

        return user

    def find_user(self, username):
        """hakee käyttäjän tietokannasta käyttäjänimen perusteella.

        Args:
            username (str): käyttäjänimi.

        Returns:
            User: haettu käyttäjä User-oliona.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        result = cursor.fetchone()

        return get_user(result)

    def get_id(self, username):
        """hakee käyttäjän id-tunnuksen tietokannasta käyttäjänimen perusteella.

        Args:
            username (str): käyttäjänimi.

        Returns:
            int: haettu käyttäjän id-tunnus.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE username = ?",
            (username,)
        )

        result = cursor.fetchone()[0]
        return result

    def get_username(self, user_id):
        """hakee käyttäjän käyttäjänimen tietokannasta id-tunnuksen perusteella.

        Args:
            user_id (int): käyttäjän id-tunnus.

        Returns:
            str: haettu käyttäjänimi.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT username FROM users WHERE id = ?",
            (user_id,)
        )

        result = cursor.fetchone()[0]
        return result

    def get_role(self, username):
        """hakee käyttäjän käyttäjäroolin tietokannasta käyttäjänimen perusteella.

        Args:
            username (str): käyttäjänimi

        Return:
            int: käyttäjärooli.
        """

        cursor = self.db_.cursor()

        cursor.execute(
            "SELECT role FROM users WHERE username = ?",
            (username,)
        )

        result = cursor.fetchone()[0]
        return result


user_repository = UserRepository(get_db())
