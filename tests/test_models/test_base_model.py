#!/usr/bin/python3
"Unit tests for BaseModel class"
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    "Unit tests suite for BaseModel class"

    def test_save(self):
        "Tests that save method updates the datetime"
        base = BaseModel()
        old_time = base.updated_at
        base.save()
        self.assertNotEqual(old_time, base.updated_at)
