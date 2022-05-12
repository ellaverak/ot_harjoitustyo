import unittest
from services.mommo_service import MommoNameLengthError, mommo_service
from services.user_service import user_service
from repositories.mommo_repository import mommo_repository
from build import build
from entities.mommo import Mommo


class TesMommoService(unittest.TestCase):
    def setUp(self):
        build()

        self.mommo_repository = mommo_repository
        self.mommo_service = mommo_service

        self.user = user_service.create_user("test", "test", 0)

    def test_create_mommo(self):
        new_mommo = self.mommo_service.create_mommo("test_mommo")

        mommo = self.mommo_repository.get(user_service.user_id)

        self.assertEqual(new_mommo.name, mommo.name)

    def test_mommo_name_length_error(self):

        with self.assertRaises(MommoNameLengthError):
            self.mommo_service.create_mommo("")

    def test_login_mommo(self):
        new_mommo = self.mommo_service.create_mommo("test_mommo")
        self.mommo_service.login_mommo()

        self.assertEqual(new_mommo.name, self.mommo_service.mommo.name)

    def test_logout_mommo(self):
        self.mommo_service.create_mommo("test_mommo")
        self.mommo_service.login_mommo()
        self.mommo_service.logout_mommo()

        self.assertEqual(self.mommo_service.mommo, None)

    def test_get_all_mommos(self):
        self.mommo_service.create_mommo("test_mommo")

        self.assertNotEqual(self.mommo_service.get_all_mommos(), None)

    def test_feed_mommo(self):
        mommo = Mommo(user_service.user_id, "test_mommo", 50, 100, 100, 100)

        self.mommo_repository.create(mommo)
        self.mommo_service.login_mommo()
        self.mommo_service.feed_mommo()
        self.assertEqual(self.mommo_service.mommo.hunger, 70)

    def test_feed_mommo_limit(self):
        mommo = Mommo(user_service.user_id, "test_mommo", 90, 100, 100, 100)

        self.mommo_repository.create(mommo)
        self.mommo_service.login_mommo()
        self.mommo_service.feed_mommo()
        self.assertEqual(self.mommo_service.mommo.hunger, 100)

    def test_water_mommo(self):
        mommo = Mommo(user_service.user_id, "test_mommo", 100, 50, 100, 100)

        self.mommo_repository.create(mommo)
        self.mommo_service.login_mommo()
        self.mommo_service.water_mommo()
        self.assertEqual(self.mommo_service.mommo.thirst, 80)

    def test_water_mommo_limit(self):
        mommo = Mommo(user_service.user_id, "test_mommo", 100, 90, 100, 100)

        self.mommo_repository.create(mommo)
        self.mommo_service.login_mommo()
        self.mommo_service.water_mommo()
        self.assertEqual(self.mommo_service.mommo.thirst, 100)

    def test_clean_mommo(self):
        mommo = Mommo(user_service.user_id, "test_mommo", 100, 100, 50, 100)

        self.mommo_repository.create(mommo)
        self.mommo_service.login_mommo()
        self.mommo_service.clean_mommo()
        self.assertEqual(self.mommo_service.mommo.clenliness, 90)

    def test_clean_mommo_limit(self):
        mommo = Mommo(user_service.user_id, "test_mommo", 100, 100, 90, 100)

        self.mommo_repository.create(mommo)
        self.mommo_service.login_mommo()
        self.mommo_service.clean_mommo()
        self.assertEqual(self.mommo_service.mommo.clenliness, 100)

    def test_do_trick_success(self):
        self.mommo_service.create_mommo("test_mommo")

        for i in range(0, 4):
            self.mommo_service.do_trick(1)

        self.assertEqual(self.mommo_service.do_trick(1), True)
