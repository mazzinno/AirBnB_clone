#!/usr/bin/python3
"""Console test"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """Console test class"""

    def create(self):
        """creating the intance"""
        return HBNBCommand()

    def test_quit(self):
        """test for the method quit"""
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """test for the method eof"""
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
