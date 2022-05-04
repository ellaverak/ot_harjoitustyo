import sys
from threading import Thread
from time import sleep
from entities.mommo import Mommo
from services.user_service import user_service

from repositories.mommo_repository import (
    mommo_repository as default_mommo_repository
)


class MommoNameLengthError(Exception):
    pass


class MommoService():
    def __init__(self, mommo_repository=default_mommo_repository):
        """luokan konstruktori, joka luo uuden mömmö-toiminnoista vastaavan palvelun.

        Args:
            mommo_repository (MommoRepository, vapaaehtoinen): MommoRepository-olio.
            Oletusarvoltaan MommoRepository-olio.
        """

        self.visit_state = False
        self.mommo = None
        self.mommo_repository = mommo_repository

        self.hunger_thread = None
        self.thirst_thread = None
        self.clenliness_thread = None
        self.happiness_thread = None

        # HUOM!! Säikeisyyden testaaminen ei ole tässä oleellista,
        # joten säikeiden aloittava funktio jätetään tässä
        # huomiotta tällä tavalla. Päädyimme pajassa ohjaaja Eetun kanssa tähän ratkaisuus.
        # Testing threads is irrelevant in this project and they are ignored.
        if "pytest" not in sys.modules and not self.visit_state:
            self.start()

    def start(self):
        """käynnistää säikeet.
        """

        self.hunger_thread = Thread(target=self.increase_hunger)
        self.hunger_thread.setDaemon(True)
        self.thirst_thread = Thread(target=self.increase_thirst)
        self.thirst_thread.setDaemon(True)
        self.clenliness_thread = Thread(target=self.decrease_clenliness)
        self.clenliness_thread.setDaemon(True)
        self.happiness_thread = Thread(target=self.decrease_happiness)
        self.happiness_thread.setDaemon(True)

        self.hunger_thread.start()
        self.thirst_thread.start()
        self.clenliness_thread.start()
        self.happiness_thread.start()

    def create_mommo(self, name):
        """luo uuden Mommo-olion, tallentaa sen tietokantaan ja asettaa nykyisen mommon.

        Args:
            name (str): uuden mömmön nimi.

        Raises:
            MommoNameLengthError: mömmön nimi on liian lyhyt eli alle 4 merkkiä.

        Returns:
            Mommo: luotu Mommo-olio.
        """

        if len(name) < 4:
            raise MommoNameLengthError(
                "Mömmön nimen on oltava vähintään neljän merkin pituinen")

        user_id = user_service.get_user_id()

        mommo = self.mommo_repository.create(Mommo(user_id, name))
        self.mommo = mommo

        return mommo

    def login_mommo(self, visit_user_id=None):
        """kirjaa mömmön sisään asettamalla sen nykyiseksi mömmöksi.

        Args:
            visit_user_id (int, vapaaehtoinen):
            käyttäjän id-tunnus, jos kyseessä on vierailu. Oletusarvoltaan None.
            visit (totuusarvo, vapaaehtoinen):
            True=vierailu, False=ei vierailu. Oletusarvoltaan False.

        Returns:
            Mommo: sisäänkirjattu Mommo-olio.
        """

        if not self.visit_state:
            user_id = user_service.get_user_id()
        else:
            user_id = visit_user_id

        mommo = self.mommo_repository.get(user_id)
        self.mommo = mommo

        return mommo

    def logout_mommo(self):
        """kirjaa nykyisen mömmön ulos.
        """

        self.save_mommo()
        self.mommo = None

    def save_mommo(self):
        self.mommo_repository.save_mommo(self.mommo)

    def get_all_mommos(self):
        """palauttaa kaikki mömmöt tietokannasta.

        Returns:
            lista: kaikki mömmöt listana [user_id, mommo, username].
        """

        user_id = user_service.get_user_id()
        result = self.mommo_repository.get_all(user_id)
        all_mommos = []

        for mommo in result:
            mommo = list(mommo)
            mommo.append(user_service.get_username(mommo[0]))

            all_mommos.append(mommo)

        return all_mommos

    def increase_hunger(self):
        """lisää mömmön nälkäisyyttä.
        """

        while True:
            if "pytest" not in sys.modules:
                sleep(360)
            if self.mommo and self.mommo.hunger > 0:
                if self.mommo.hunger - 10 > 0:
                    self.mommo.hunger = self.mommo.hunger - 10
                else:
                    self.mommo.hunger = 0

    def increase_thirst(self):
        """lisää mömmön janoisuutta.
        """

        while True:
            sleep(60)
            if self.mommo and self.mommo.thirst > 0:
                if self.mommo.thirst - 10 > 0:
                    self.mommo.thirst = self.mommo.thirst - 10
                else:
                    self.mommo.thirst = 0

    def decrease_clenliness(self):
        """vähentää mömmön puhtautta.
        """

        while True:
            sleep(120)
            if self.mommo and self.mommo.clenliness > 0:
                if self.mommo.clenliness - 40 > 0:
                    self.mommo.clenliness = self.mommo.clenliness - 40
                else:
                    self.mommo.clenliness = 0

    def decrease_happiness(self):
        """vähentää mömmön onnellisuutta.
        """

        while True:
            sleep(360)
            if self.mommo and self.mommo.happiness > 0:
                self.mommo.happiness = int(
                    self.mommo.hunger * 0.3
                    + self.mommo.thirst * 0.3 + self.mommo.thirst * 0.4)

    def feed_mommo(self):
        """vähentää mömmön nälkäisyyttä 20 yksikköä.
        """

        if self.mommo.hunger + 20 <= 100:
            self.mommo.hunger += 20
        else:
            self.mommo.hunger = 100

        self.save_mommo()

    def water_mommo(self):
        """vähentää mömmön janoisuutta 30 yksikköä.
        """

        if self.mommo.thirst + 30 <= 100:
            self.mommo.thirst += 30
        else:
            self.mommo.thirst = 100

        self.save_mommo()

    def clean_mommo(self):
        """lisää mömmön puhtautta 40 yksikköä.
        """

        if self.mommo.clenliness + 40 <= 100:
            self.mommo.clenliness += 40
        else:
            self.mommo.clenliness = 100

        self.save_mommo()


mommo_service = MommoService()
