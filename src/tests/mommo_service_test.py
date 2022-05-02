import unittest
from services.mommo_service import mommo_service
from services.user_service import user_service
from repositories.mommo_repository import mommo_repository
from build import build
from entities.user import User
from entities.mommo import Mommo


class TesMommoService(unittest.TestCase):
    def setUp(self):
        build()

        self.mommo_repository = mommo_repository
        self.mommo_service = mommo_service

    def test_create_mommo(self):
        return
