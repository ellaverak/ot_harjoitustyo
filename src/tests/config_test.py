import unittest
from build import build
from build import build as build_
import db_connection


class TestConfig(unittest.TestCase):
    def setUp(self):
        build()

    def test_build(self):
        build_()
        self.assertNotEqual(db_connection.get_db, None)
