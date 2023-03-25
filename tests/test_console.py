#!/usr/bin/python3
"""Unittest for Amenity
"""
import unittest
import pycodestyle
import unittest.mock


class TestConsole(unittest.TestCase):
    """Class to test Console
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_Documentation(self):
        """Test if module BaseModel has documentation
        """
        self.assertTrue(len(self.console.__doc__) > 0)
