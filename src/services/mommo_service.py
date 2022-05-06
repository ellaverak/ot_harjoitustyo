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

        self._hunger_thread = None
        self._thirst_thread = None
        self._clenliness_thread = None

        # HUOM!! Säikeisyyden testaaminen ei ole tässä oleellista,
        # joten säikeiden aloittava funktio jätetään tässä
        # huomiotta tällä tavalla. Päädyimme pajassa ohjaaja Eetun kanssa tähän ratkaisuus.
        # Testing threads is irrelevant in this project and they are ignored.
        if "pytest" not in sys.modules and not self.visit_state:
            self._start()

    def _start(self):
        """käynnistää säikeet.
        """

        self._hunger_thread = Thread(target=self._decrease_hunger_stat)
        self._hunger_thread.setDaemon(True)
        self._thirst_thread = Thread(target=self._decrease_thirst_stat)
        self._thirst_thread.setDaemon(True)
        self._clenliness_thread = Thread(target=self._decrease_clenliness_stat)
        self._clenliness_thread.setDaemon(True)

        self._hunger_thread.start()
        self._thirst_thread.start()
        self._clenliness_thread.start()

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

    def get_mommo_id(self):

        mommo_id = self.mommo_repository.get_id(user_service.get_user_id())
        return mommo_id

    def _decrease_hunger_stat(self):
        """lisää mömmön nälkäisyyttä.
        """

        while True:
            if "pytest" not in sys.modules:
                sleep(120)
            if self.mommo and self.mommo.hunger > 0:
                if self.mommo.hunger - 10 > 0:
                    self.mommo.hunger = self.mommo.hunger - 10
                else:
                    self.mommo.hunger = 0

                self._calculate_happiness_stat()

    def _decrease_thirst_stat(self):
        """lisää mömmön janoisuutta.
        """

        while True:
            sleep(60)
            if self.mommo and self.mommo.thirst > 0:
                if self.mommo.thirst - 10 > 0:
                    self.mommo.thirst = self.mommo.thirst - 10
                else:
                    self.mommo.thirst = 0

                self._calculate_happiness_stat()

    def _decrease_clenliness_stat(self):
        """vähentää mömmön puhtautta.
        """

        while True:
            sleep(140)
            if self.mommo and self.mommo.clenliness > 0:
                if self.mommo.clenliness - 40 > 0:
                    self.mommo.clenliness = self.mommo.clenliness - 40
                else:
                    self.mommo.clenliness = 0

                self._calculate_happiness_stat()

    def _calculate_happiness_stat(self):
        """vähentää mömmön onnellisuutta.
        """

        if self.mommo and self.mommo.happiness > 0:
            if int(self.mommo.hunger * 0.3
                   + self.mommo.thirst + 0.3 + self.mommo.clenliness * 0.4) <= 100:
                self.mommo.happiness = int(self.mommo.hunger * 0.3
                                           + self.mommo.thirst + 0.3 + self.mommo.clenliness * 0.4)
            elif int(self.mommo.hunger * 0.3
                     + self.mommo.thirst + 0.3 + self.mommo.clenliness * 0.4) > 100:
                self.mommo.happiness = 100

    def feed_mommo(self):
        """vähentää mömmön nälkäisyyttä 20 yksikköä.
        """

        if self.mommo.hunger + 20 <= 100:
            self.mommo.hunger += 20
        else:
            self.mommo.hunger = 100

        self._calculate_happiness_stat()
        self.save_mommo()

    def water_mommo(self):
        """vähentää mömmön janoisuutta 30 yksikköä.
        """

        if self.mommo.thirst + 30 <= 100:
            self.mommo.thirst += 30
        else:
            self.mommo.thirst = 100

        self._calculate_happiness_stat()
        self.save_mommo()

    def clean_mommo(self):
        """lisää mömmön puhtautta 40 yksikköä.
        """

        if self.mommo.clenliness + 40 <= 100:
            self.mommo.clenliness += 40
        else:
            self.mommo.clenliness = 100

        self._calculate_happiness_stat()
        self.save_mommo()

    def do_trick(self, trick):
        mommo_id = self.get_mommo_id()

        trick_list = self.mommo_repository.get_trick(mommo_id)

        if trick == 1:
            if trick_list[0] < 100:
                if trick_list[0] + 25 > 100:
                    trick_list[0] = 100
                else:
                    trick_list[0]+=25

                self.mommo_repository.save_trick(mommo_id, trick_list)
                return "Mömmö harjoittelee..."

            return "Mömmö hyppäsi! :D"

        if trick == 2:
            if trick_list[1] < 100:
                if trick_list[1] + 25 > 100:
                    trick_list[1] = 100
                else:
                    trick_list[1]+=25

                self.mommo_repository.save_trick(mommo_id, trick_list)
                return "Mömmö harjoittelee..."

            return "Mömmö litistyi! :P"

        if trick == 3:
            if trick_list[2] < 100:
                if trick_list[2] + 25 > 100:
                    trick_list[2] = 100
                else:
                    trick_list[2]+=25

                self.mommo_repository.save_trick(mommo_id, trick_list)
                return "Mömmö harjoittelee..."

            return "Mömmö leikki kuollutta! X)"


mommo_service = MommoService()
