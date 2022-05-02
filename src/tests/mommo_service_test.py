import unittest
from services.mommo_service import MommoNameLengthError, mommo_service
from services.user_service import user_service
from repositories.mommo_repository import mommo_repository
from build import build

class TesMommoService(unittest.TestCase):
    def setUp(self):
        build()

        self.mommo_repository = mommo_repository
        self.mommo_service = mommo_service

        self.user = user_service.create_user("test", "test", 0)

    def test_create_mommo(self):
        new_mommo = self.mommo_service.create_mommo("test_mommo")

        mommo = self.mommo_repository.get(user_service.get_user_id())

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