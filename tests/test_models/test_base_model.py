#!/usr/bin/python3
"""Unit test for testing BaseModel class"""
import unittest
import datetime
from uuid import UUID
import json
from os import getenv, remove
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class"""

    def setUp(self):
        """Set up"""
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """Tear down"""
        try:
            remove('file.json')
        except:
            pass

    def test_default(self):
        """Test default values of instance"""
        self.assertIsInstance(self.model1, BaseModel)

    def test_kwargs(self):
        """Test creation of an instance with dictionary"""
        model_dict = self.model1.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertFalse(new_model is self.model1)

    def test_kwargs_int(self):
        """Test method dictionary and update method"""
        model_dict = self.model1.to_dict()
        model_dict.update({1: 2})
        with self.assertRaises(TypeError):
            new_model = BaseModel(**model_dict)

    def test_str(self):
        """Check str format"""
        string = str(self.model1)
        self.assertIsInstance(string, str)

    def test_to_dict(self):
        """Test to_dict method"""
        dict_obj = self.model1.to_dict()
        self.assertIsInstance(dict_obj, dict)

    def test_kwargs_none(self):
        """Test dictionary with none arguments"""
        with self.assertRaises(TypeError):
            new_model = BaseModel(None)

    def test_kwargs_one(self):
        """Test dictionary with arguments"""
        n = {'name': 'test'}
        new_model = BaseModel(**n)
        self.assertEqual(type(new_model), BaseModel)

    def test_id(self):
        """Test id of the instance"""
        self.assertEqual(type(self.model1.id), str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_created_at(self):
        """Test creation of the instance"""
        self.assertEqual(type(self.model1.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test update method"""
        model_dict = self.model1.to_dict()
        new_model = BaseModel(**model_dict)
        new_model.save()
        self.assertNotEqual(new_model.created_at, new_model.updated_at)
