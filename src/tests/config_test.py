import unittest
from build import build
import db_connection


class TestConfig(unittest.TestCase):
    def setUp(self):
        build()

    def test_build(self):
        self.assertNotEqual(db_connection.get_db(), None)
