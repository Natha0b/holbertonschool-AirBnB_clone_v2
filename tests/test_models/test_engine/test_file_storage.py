#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import inspect
import pep8
from unittest.case import skipIf


@skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
        'skip in case is db_storage')
class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.skipTest('Using DB Storage')
        else:
            del_list = []
            for key in storage._FileStorage__objects.keys():
                del_list.append(key)
            for key in del_list:
                del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        self.assertTrue(storage.all() != {})

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        new.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        new2.save()
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        new.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        new.save()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

    def test_delete(self):
        """ Delete method from file_storage functioning properly """
        new = BaseModel()
        new.save()
        storage.delete(new)
        self.assertEqual(storage.all(), {})


class TestFileStorageDoc(unittest.TestCase):
    "Tests documentation and pep8 for FileStorage class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class FileStorage to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(FileStorage,
                                           inspect.isfunction(FileStorage))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models.engine import file_storage

        self.assertTrue(len(file_storage.__doc__) > 0)
        self.assertTrue(len(file_storage.FileStorage.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")