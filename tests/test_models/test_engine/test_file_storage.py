#!/usr/bin/python3
"""Unit testing module for FileStorage class"""

import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_class(unittest.TestCase):
    """unittests for FileStorage class"""

    def test_class_type(self):
        """method tests class type"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

    def testFileStorage_objects_is_private(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all_method_type(self):
        """method tests all method in FileStorage"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_arg(self):
        """method tests all method by passing an arguement"""
        with self.assertRaises(TypeError):
            models.storage.all(BaseModel(None))

    def test_new_method_with_None(self):
        """method tests new method by passing None"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_method_with_args(self):
        """method tests new method by passing a parameter"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_method(self):
        """method tests adding a new object to FileStorage"""
        bs = BaseModel()
        cy = City()
        am = Amenity()
        rev = Review()
        plc = Place()
        st = State()
        usr = User()
        newDict = {
            bs: "BaseModel.",
            cy: "City.",
            am: "Amenity.",
            rev: "Review.",
            plc: "Place.",
            st: "State.",
            usr: "User."
        }
        for var, cls in newDict.items():
            models.storage.new(var)
            self.assertIn(cls + var.id, models.storage.all().keys())
            self.assertIn(var, models.storage.all.values())

    def test_save_method_with_arg(self):
        """method tests passing a None arg to save method"""
        with self.assertRaises(TypeError):
            models.storage.save(BaseModel(None))

    def test_save_method(self):
        """method tests save an object to json file"""
        bs = BaseModel()
        cy = City()
        am = Amenity()
        rev = Review()
        plc = Place()
        st = State()
        usr = User()
        newDict = {
            bs: "BaseModel.",
            cy: "City.",
            am: "Amenity.",
            rev: "Review.",
            plc: "Place.",
            st: "State.",
            usr: "User."
        }
        for var in newDict.keys():
            models.storage.new(var)
        models.storage.save()
        file_text = ""
        with open("file.json", "r") as f:
            file_text = f.read()
            for var, cls in newDict.items():
                self.assertIn(cls + var.id, file_text)

    def test_reload_with_arg(self):
        """method tests passing a None arg to reload method"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_method(self):
        """method tests reload an object from json file"""
        bs = BaseModel()
        cy = City()
        am = Amenity()
        rev = Review()
        plc = Place()
        st = State()
        usr = User()
        newDict = {
            bs: "BaseModel.",
            cy: "City.",
            am: "Amenity.",
            rev: "Review.",
            plc: "Place.",
            st: "State.",
            usr: "User."
        }
        for var in newDict.keys():
            models.storage.new(var)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        for var, cls in newDict.items():
            self.assertIn(cls + var.id, objects)
