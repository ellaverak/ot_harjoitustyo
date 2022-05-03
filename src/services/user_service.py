from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class UsernameExistsError(Exception):
    pass


class PasswordLengthError(Exception):
    pass


class UsernameLengthError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserNonexistingError(Exception):
    pass


class UserService():
    def __init__(self, user_repository=default_user_repository):
        """luokan konstruktori, joka luo uuden käyttäjätoiminnoista vastaavan palvelun.

        Args:
            user_repository (UserRepository, vapaaehtoinen):
            UserRepository-olio. Oletusarvoltaan UserRepository-olio.
        """

        self.user = None
        self.visit_id = None
        self.user_repository = user_repository

    def create_user(self, username, password, role):
        """luo uuden User-olion ja tallentaa sen tietokantaan.

        Args:
            username (str): uusi käyttäjänimi.
            password (str): uusi salasana.
            role (int): käyttäjärooli. 0=tavallinen käyttäjä, 1=ylläpitäjä.

        Raises:
            UsernameExistsError: käyttäjänimi löytyy jo tietokannasta eli se on varattu.
            PasswordLengthError: salasana on liian lyhyt eli alle 4 merkkiä.
            UsernameLengthError: käyttäjänimi on liian lyhyt eli alle 4 merkkiä.

        Returns:
            User: luotu User-olio.
        """

        if self.user_repository.find_user(username):
            raise UsernameExistsError("Käyttäjätunnus on jo käytössä")

        if len(password) < 4:
            raise PasswordLengthError(
                "Salasanan on oltava vähintään neljän merkin pituinen")

        if len(username) < 4:
            raise UsernameLengthError(
                "Käyttäjätunnuksen on oltava vähintään neljän merkin pituinen")

        self.user_repository.create(User(username, password, role))
        user = self.login(username, password)

        return user

    def login(self, username, password):
        """kirjaa käyttäjän sisään asettamalla sen nykyiseksi käyttäjäksi.

        Args:
            username (str): käyttäjänimi.
            password (str): salasana.

        Raises:
            UserNonexistingError:
            käyttäjänimeä ei löydy tietokannasta eli käyttäjää ei ole olemassa.
            WrongPasswordError: väärä salasana.

        Returns:
            User: sisäänkirjattu User-olio.
        """

        user = self.user_repository.find_user(username)

        if not user:
            raise UserNonexistingError("Käyttäjätunnusta ei ole olemassa")

        if user.password != password:
            raise WrongPasswordError("Väärä salasana")

        self.user = user

        return user

    def logout(self):
        """kirjaa nykyisen käyttäjän ulos.
        """

        self.user = None

    def get_user_id(self):
        """hakee nykyisen käyttäjän id-tunnuksen käyttäjänimen perusteella.

        Returns:
            int: nykyisen käyttäjän id-tunnus.
        """

        user_id = self.user_repository.get_id(self.user.username)
        return user_id

    def get_username(self, user_id):
        """hakee nykyisen käyttäjän käyttäjänimen id-tunnuksen perusteella.

        Args:
            user_id (int): käyttäjän id-tunnus.

        Returns:
            str: nykyisen käyttäjän käyttäjänimi.
        """

        user_name = self.user_repository.get_username(user_id)
        return user_name

    def get_role(self):
        """hakee nykyisen käyttäjän käyttäjäroolin käyttäjänimen perusteella.

        Returns:
            int: nykyisen käyttäjän käyttäjärooli.
        """

        role = self.user_repository.get_role(self.user.username)
        return role

    def visit(self, user_id):
        """asettaa vierailtavan käyttäjän id-tunnuksen.

        Args:
            user_id (int): vierailtavan käyttäjän id-tunnus.
        """

        self.visit_id = user_id


user_service = UserService()
