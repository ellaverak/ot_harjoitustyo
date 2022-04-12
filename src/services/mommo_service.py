from entities.mommo import Mommo
from services.user_service import user_service
from repositories.user_repository import user_repository

from repositories.mommo_repository import (
    mommo_repository as default_mommo_repository
)

class MommoService():
    def __init__(self, mommo_repository=default_mommo_repository):
        self.mommo = None
        self.mommo_repository = mommo_repository

    def create_mommo(self, name):
        user = user_service.user
        user_id = user_repository.get_id(user.username)

        mommo = self.mommo_repository.create(Mommo(user_id, name))

        return mommo

mommo_service = MommoService()