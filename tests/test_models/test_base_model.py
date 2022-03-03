#!/usr/bin/python3
""" Unittest of Base class"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test of class Base """

    def test_id(self):
        """test for id attribute of BaseModel
        """
        b = BaseModel()
        self.assertEqual(type(b.id), type("abc"))

    def test_created_at(self):
        """test for created_at attribute of base
        """
        b = BaseModel()
        d = datetime.now()
        self.assertEqual(str(b.created_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_updated_at(self):
        """test for updated_at attribute of base
        """
        b = BaseModel()
        d = datetime.now()
        self.assertEqual(str(b.updated_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_name(self):
        """test for name attribute of base
        """
        b = BaseModel()
        b.name = "test"
        self.assertEqual(b.name, "test")

    def test_name2(self):
        """test for name attribute of base
        """
        b = BaseModel()
        b.name = ""
        self.assertEqual(b.name, "")

if __name__ == "__main__":
    unittest.main()