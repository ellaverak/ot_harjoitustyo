from entities.mommo import Mommo
from services.user_service import user_service

from repositories.mommo_repository import (
    mommo_repository as default_mommo_repository
)


class MommoService():
    def __init__(self, mommo_repository=default_mommo_repository):
        self.mommo = None
        self.mommo_repository = mommo_repository

    def create_mommo(self, name):
        user_id = user_service.get_user_id()

        mommo = self.mommo_repository.create(Mommo(user_id, name))

        self.mommo = mommo

        return mommo

    def login_mommo(self):
        user_id = user_service.get_user_id()

        mommo = self.mommo_repository.get(user_id)

        self.mommo = mommo

        return mommo

    def logout_mommo(self):
        self.mommo_repository.save_mommo(self.mommo)
        self.mommo = None

    def hunger(self):
        if self.mommo.hunger - 10 > 0:
            self.mommo.hunger = self.mommo.hunger - 10
        else:
            self.mommo.hunger = 0

    def feed_mommo(self):
        #limit!
        self.mommo.hunger+=20
        self.mommo_repository.save_mommo(self.mommo)

    def water_mommo(self):
        #limit!
        self.mommo.thirst+=30
        self.mommo_repository.save_mommo(self.mommo)


mommo_service = MommoService()
