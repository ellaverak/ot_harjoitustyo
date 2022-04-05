from entities.mommo import Mommo

from repositories.mommo_repository import (
    mommo_repository as default_mommo_repository
)

class MommoService():
    def __init__(self, mommo_repository=default_mommo_repository):
        self.mommo = None
        self.mommo_repository = mommo_repository

    def create_mommo(self, user_id, name, hunger, thirst, clenliness, happiness):

        mommo = self.user_repository.create(Mommo(user_id, name, hunger, thirst, clenliness, happiness))

        return mommo

mommo_service = MommoService()