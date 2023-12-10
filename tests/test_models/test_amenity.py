#!/usr/bin/python3
"""Unittest module for Amenity class"""

import models
from models.amenity import Amenity
import unittest
from datetime import datetime


class TestAmenity_class(unittest.TestCase):
    """unittests for Amenity class"""

    def test_no_args_instantiates(self):
        """method tests instance with no args"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """method tests instance stored in dict"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """method check for id is public"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_args_unused(self):
        """method tests unused args"""
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_class_instances(self):
        """method that tests all class instances"""
        am = Amenity()

        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(am))
        self.assertNotIn("name", am.__dict__)

    def test_str_method(self):
        """method test the str method has the correct output"""
        am = Amenity()
        string = "[Amenity] ({}) {}".format(am.id, am.__dict__)
        self.assertEqual(string, str(am))

    def test_to_dict_contains_added_attributes(self):
        """method tests add attr"""
        am = Amenity()
        am.mid_name = "ALX"
        am.num = 15
        self.assertEqual("ALX", am.mid_name)
        self.assertIn("num", am.to_dict())

    def test_to_dict_attrs_strs(self):
        """method tests type of instance of an object after calling to_dict"""
        am = Amenity()
        newDict = am.to_dict()
        self.assertEqual(str, type(newDict["id"]))
        self.assertEqual(str, type(newDict["updated_at"]))
        self.assertEqual(str, type(newDict["created_at"]))

    def test_save_updates_file(self):
        """method tests checks for class id into json file"""
        am = Amenity()
        am.save()
        am_id = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(am_id, f.read())
