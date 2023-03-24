#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for console.py"""
from console import HBNBCommand

from unittest import TestCase
import inspect
import pep8


class TestHBNBCommandDoc(TestCase):
    "Tests documentation and pep8 for HBNBCommand class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class HBNBCommand to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(HBNBCommand,
                                           inspect.isfunction(HBNBCommand))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        import console

        self.assertTrue(len(console.__doc__) > 0)
        self.assertTrue(len(console.HBNBCommand.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
