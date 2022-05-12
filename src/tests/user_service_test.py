import unittest
from services.user_service import UserNonexistingError, WrongPasswordError, UsernameExistsError, UsernameLengthError, PasswordLengthError, user_service
from repositories.user_repository import user_repository
from build import build
from entities.user import User


class TestUserService(unittest.TestCase):
    def setUp(self):
        build()

        self.user_repository = user_repository
        self.user_service = user_service

    def test_create_user(self):
        new_user = self.user_service.create_user("test", "test", 0)

        user = user_repository.find_user(new_user.username)

        self.assertEqual(new_user.username, user.username)

    def test_username_exists_error(self):
        self.user_service.create_user("test", "test", 0)

        with self.assertRaises(UsernameExistsError):
            self.user_service.create_user("test", "test", 0)

    def test_username_length_error(self):

        with self.assertRaises(UsernameLengthError):
            self.user_service.create_user("", "test", 0)

    def test_password_length_error(self):

        with self.assertRaises(PasswordLengthError):
            self.user_service.create_user("test", "", 0)

    def test_login(self):
        user = User("login_test", "login_test", 1)
        self.user_service.create_user(user.username, user.password, user.role)

        logged_in_user = self.user_service.login(user.username, user.password)

        self.assertEqual(logged_in_user.username, user.username)

    def test_logout(self):
        user = User("login_test", "login_test", 1)
        self.user_service.create_user(user.username, user.password, user.role)

        self.user_service.logout()

        self.assertEqual(user_service.user, None)

    def test_login_username_error(self):

        with self.assertRaises(UserNonexistingError):
            self.user_service.login(
                user_service.user.username, user_service.user.password)

    def test_login_password_error(self):
        self.user_service.create_user("test", "test", 0)

        with self.assertRaises(WrongPasswordError):
            self.user_service.login(user_service.user.username, "pass")

    def test_get_username(self):
        self.user_service.create_user("test", "test", 0)
        username = self.user_service.get_username(self.user_service.user_id)

        self.assertEqual(username, "test")

    def test_get_role(self):
        self.user_service.create_user("test", "test", 1)
        role = self.user_service.get_role()

        self.assertEqual(role, 1)

    def test_visit(self):
        self.user_service.visit(2)

        self.assertEqual(self.user_service.visit_id, 2)
