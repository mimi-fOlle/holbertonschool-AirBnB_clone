#!/usr/bin/pyhon3
"Unit Tests for User class"
import unittest
from models.user import User
from models.base_model import BaseModel
import models


class TestUser(unittest.TestCase):
    "Unit tests suite for User class"

    def test_instance(self):
        "Test instance"
        Holbie = User()
        self.assertIsInstance(Holbie, User)

    def test_email(self):
        "Test email"
        Holbie = User()
        self.assertEqual("", Holbie.email)

    def test_password(self):
        "Test password"
        Holbie = User()
        self.assertEqual("", Holbie.password)

    def test_first_name(self):
        "Test first name"
        Holbie = User()
        self.assertEqual("", Holbie.first_name)

    def test_last_name(self):
        "Test last name"
        Holbie = User()
        self.assertEqual("", Holbie.last_name)
