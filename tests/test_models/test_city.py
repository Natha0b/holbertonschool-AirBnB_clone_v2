#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ test of model city """

    def __init__(self, *args, **kwargs):
        """Initialize """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ check state id """
        new = self.value(state_id='1111n92')
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """check name """
        new = self.value(name='Los Angeles')
        self.assertEqual(type(new.name), str)
