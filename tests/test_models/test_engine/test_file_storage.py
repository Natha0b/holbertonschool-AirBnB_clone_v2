#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        storage._FileStorage__objects = {}

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        key = new.__class__.__name__ + "." + str(new.id)
        self.assertIn(key, storage.all().keys())

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(new, all_objs.values())

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        all_objs = storage.all()
        key = new.__class__.__name__ + "." + str(new.id)
        self.assertIn(key, all_objs.keys())

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertIsNone(storage.reload())

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertIsInstance(storage.all(), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        key = new.__class__.__name__ + "." + str(new.id)
        self.assertEqual(list(storage.all().keys())[0], key)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(storage, FileStorage)
