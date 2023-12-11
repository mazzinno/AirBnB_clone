#!/usr/bin/python3
"""Test case for FileStorage module"""
import unittest
import os
import contextlib
import json
import models
import pep8
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test for FileStorage
    """

    def test_pep8_FileStorage(self):
        """Tests pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def setUp(self):
        """Sets up class test"""

        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        """
        Tears down testing environment
        """

        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Check the all"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """
        check the storage if is not empty
        """

        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """
        check the type of storage
        """

        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """
        check the new user
        """
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "Julien"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """
        Checks if methods from 
        Storage Engine works.
        """

        with open("file.json") as f:
            dic = json.load(f)

            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """
        Checking if methods from Storage Engine works.
        """

        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """
        Check the docString each function
        """

        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))


if __name__ == '__main__':
    unittest.main()
