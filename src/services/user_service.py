from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserService():
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, role):

        user = self._user_repository.create(User(username, password, role))

        return user


user_service = UserService()
