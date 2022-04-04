from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserService():
    def __init__(self, user_repository=default_user_repository):
        self.user = None
        self.user_repository = user_repository

    def create_user(self, username, password, role):

        user = self.user_repository.create(User(username, password, role))

        return user

    def login(self, username, password):

        user = self.user_repository.find_user(username)

        if not user or user.password != password:
            #error
            print("error")
            return

        self.user = user

        return user


user_service = UserService()
