from time import sleep
from threading import Thread
from entities.mommo import Mommo
from services.user_service import user_service

from repositories.mommo_repository import (
    mommo_repository as default_mommo_repository
)


class MommoService():
    def __init__(self, mommo_repository=default_mommo_repository):
        self.mommo = None
        self.mommo_repository = mommo_repository

        self.hunger_thread = Thread(target=self.increase_hunger)
        self.thirst_thread = Thread(target=self.increase_thirst)
        self.clenliness_thread = Thread(target=self.decrease_clenliness)
        self.happiness_thread = Thread(target=self.decrease_happiness)

        self.start()

    def start(self):
        self.hunger_thread.start()
        self.thirst_thread.start()
        self.clenliness_thread.start()
        self.happiness_thread.start()

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

    def increase_hunger(self):
        while True:
            sleep(120)
            if self.mommo and self.mommo.hunger > 0:
                if self.mommo.hunger - 10 > 0:
                    self.mommo.hunger = self.mommo.hunger - 10
                else:
                    self.mommo.hunger = 0

    def increase_thirst(self):
        while True:
            sleep(30)
            if self.mommo and self.mommo.thirst > 0:
                if self.mommo.thirst - 10 > 0:
                    self.mommo.thirst = self.mommo.thirst - 10
                else:
                    self.mommo.thirst = 0

    def decrease_clenliness(self):
        while True:
            sleep(360)
            if self.mommo and self.mommo.clenliness > 0:
                if self.mommo.clenliness - 40 > 0:
                    self.mommo.clenliness = self.mommo.clenliness - 40
                else:
                    self.mommo.clenliness = 0

    def decrease_happiness(self):
        while True:
            sleep(1)
            if self.mommo and self.mommo.happiness > 0:
                self.mommo.happiness = int(
                    self.mommo.hunger * 0.3 + self.mommo.thirst * 0.3 + self.mommo.thirst * 0.4)

    def feed_mommo(self):
        if self.mommo.hunger + 20 <= 100:
            self.mommo.hunger += 20
        else:
            self.mommo.hunger = 100

        self.mommo_repository.save_mommo(self.mommo)

    def water_mommo(self):
        if self.mommo.thirst + 30 <= 100:
            self.mommo.thirst += 30
        else:
            self.mommo.thirst = 100

        self.mommo_repository.save_mommo(self.mommo)

    def clean_mommo(self):
        if self.mommo.clenliness + 40 <= 100:
            self.mommo.clenliness += 40
        else:
            self.mommo.clenliness = 100

        self.mommo_repository.save_mommo(self.mommo)


mommo_service = MommoService()
