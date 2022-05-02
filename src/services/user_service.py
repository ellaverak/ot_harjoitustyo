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
        self.user = None
        self.user_repository = user_repository

    def create_user(self, username, password, role):

        if self.user_repository.find_user(username):
            raise UsernameExistsError(f"Käyttäjätunnus on jo käytössä")

        if len(password) < 4:
            raise PasswordLengthError(
                f"Salasanan on oltava vähintään neljän merkin pituinen")

        if len(username) < 4:
            raise UsernameLengthError(
                f"Käyttäjätunnuksen on oltava vähintään neljän merkin pituinen")

        self.user_repository.create(User(username, password, role))
        user = self.login(username, password)

        return user

    def login(self, username, password):

        user = self.user_repository.find_user(username)

        if not user:
            raise UserNonexistingError(f"Käyttäjätunnusta ei ole olemassa")

        if user.password != password:
            raise WrongPasswordError(F"Väärä salasana")

        self.user = user

        return user

    def logout(self):
        self.user = None

    def get_user_id(self):
        user_id = self.user_repository.get_id(self.user.username)
        return user_id


user_service = UserService()
