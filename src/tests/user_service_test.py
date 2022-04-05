import unittest
from services.user_service import user_service
from repositories.user_repository import user_repository
from build import build

class TestUserService(unittest.TestCase):
    def setUp(self):
        build()

        self.user_repository = user_repository
        self.user_service = user_service

    def test_create_user(self):
        new_user = self.user_service.create_user("test", "test", 0)

        user = user_repository.find_user(new_user.username)

        self.assertEqual(new_user.username, user.username)