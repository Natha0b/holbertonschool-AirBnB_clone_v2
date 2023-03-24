#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ test user """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ check first name """
        new = self.value(first_name='John')
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ check last name """
        new = self.value(last_name='Doe')
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(email='johndoe@johndoe.com')
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(password='johndoe123')
        self.assertEqual(type(new.password), str)
