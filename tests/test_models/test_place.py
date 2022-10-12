#!/usr/bin/python3
"Unit tests for Place class"
import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    "Unit tests suite for Place class"
	
    def test_instance(self):
        "Test instance"
        miami = Place()
        self.assertIsInstance(miami, Place)

    def test_name(self):
        "Test place name"
        miami = Place()
        self.assertEqual("", miami.name)

    def test_city_id(self):
        "Test city id"
        miami = Place()
        self.assertEqual("", miami.city_id)

    def test_user_id(self):
        "Test user id)"
        miami = Place()
        self.assertEqual("", miami.user_id)

    def test_amenity_ids(self):
        "Test amenity id"
        miami = Place()
        self.assertEqual([], miami.amenity_ids)
