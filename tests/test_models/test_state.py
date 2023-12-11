#!/usr/bin/python3
"""test State class Module"""
import unittest
import json
import pep8
import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Testing State class implementation
    """
    def test_doc_module(self):
        """
        the Module documentation
        """
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_state(self):
        """
        Test that models/state.py conforms to pycodestyle
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """
        Test that tests/test_models/test_state.py conforms to pycodestyle
        """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        the Constructor documentation
        """
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Validating the types of the attributes an class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
