#!/usr/bin/python3
"""Unittest module for User class"""

import models
from models.user import User
import unittest
from datetime import datetime


class TestUser_class(unittest.TestCase):
    """unittests for User class"""

    def test_no_args_instantiates(self):
        """method tests instance with no args"""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """method tests instance stored in dict"""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """method check for id is public"""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_name_is_public_class_attr(self):
        usr = User()
        self.assertEqual(str, type(User.name))
        self.assertIn("name", dir(usr))
        self.assertNotIn("name", usr.__dict__)

    def test_instant_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_class_instances(self):
        """method that tests all class instances"""
        usr = User()

        self.assertEqual(str, type(User.first_name))
        self.assertIn("first_name", dir(usr))
        self.assertNotIn("first_name", usr.__dict__)

        self.assertEqual(str, type(User.last_name))
        self.assertIn("last_name", dir(usr))
        self.assertNotIn("last_name", usr.__dict__)

        self.assertEqual(str, type(User.password))
        self.assertIn("password", dir(usr))
        self.assertNotIn("password", usr.__dict__)

        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(usr))
        self.assertNotIn("email", usr.__dict__)

    def test_args_unused(self):
        """method tests unused args"""
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_str_method(self):
        """method test the str method has the correct output"""
        usr = User()
        string = "[User] ({}) {}".format(usr.id, usr.__dict__)
        self.assertEqual(string, str(usr))

    def test_to_dict_contains_added_attributes(self):
        """method tests add attr"""
        usr = User()
        usr.mid_name = "ALX"
        usr.num = 15
        self.assertEqual("ALX", usr.mid_name)
        self.assertIn("num", usr.to_dict())

    def test_to_dict_attrs_strs(self):
        """method tests type of instance of an object after calling to_dict"""
        usr = User()
        newDict = usr.to_dict()
        self.assertEqual(str, type(newDict["id"]))
        self.assertEqual(str, type(newDict["updated_at"]))
        self.assertEqual(str, type(newDict["created_at"]))

    def test_save_updates_file(self):
        """method tests checks for class id into json file"""
        usr = User()
        usr.save()
        usr_id = "User." + usr.id
        with open("file.json", "r") as f:
            self.assertIn(usr_id, f.read())
