#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import Base
from models.state import State
from models.engine.db_storage import DBStorage
from models import storage
import os
import inspect
import pep8
import MySQLdb
from unittest.case import skipIf


class TestDBStorageDoc(unittest.TestCase):
    "Tests documentation and pep8 for DBStorage class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class DBStorage to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(DBStorage,
                                           inspect.isfunction(DBStorage))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models.engine import db_storage

        self.assertTrue(len(db_storage.__doc__) > 0)
        self.assertTrue(len(db_storage.DBStorage.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/engine/db_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(
            ['tests/test_models/test_engine/test_db_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
