import unittest
from services.mommo_service import mommo_service
from services.user_service import user_service
from repositories.mommo_repository import mommo_repository
from repositories.user_repository import user_repository
from build import build
from entities.user import User


class TestUserService(unittest.TestCase):
    def setUp(self):
        build()

        self.mommo_repository = mommo_repository
        self.mommo_service = mommo_service
        self.user_service = user_service

        self.user = user_service.create_user("create_mommo", "create_mommo", 0)
