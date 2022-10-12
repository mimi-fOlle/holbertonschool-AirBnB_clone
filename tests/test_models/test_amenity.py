#!/usr/bin/python3
"Unit tests for Amenity class"
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    "Unit tests suite for Amenity class"

    def test_instance(self):
        "Test instance"
        hello = Amenity()
        self.assertIsInstance(hello, Amenity)

    def test_amenity_name(self):
        "Test amenity name"
        hello = Amenity()
        self.assertEqual("", hello.name)

    def test_amenity_id(self):
        "Test id"
        hello = Amenity()
        self.assertEqual(str, type(hello.id))
