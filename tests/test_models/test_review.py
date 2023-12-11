#!/usr/bin/python3
"""Unittest module for Review class"""

import models
from models.review import Review
import unittest
from datetime import datetime


class TestReview_class(unittest.TestCase):
    """unittests for Review class"""

    def test_no_args_instantiates(self):
        """method tests instance with no args"""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """method tests instance stored in dict"""
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        """method check for id is public"""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_name_is_public_class_attr(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_instant_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_class_instances(self):
        """method that tests all class instances"""
        rev = Review()

        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_args_unused(self):
        """method tests unused args"""
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_str_method(self):
        """method test the str method has the correct output"""
        rev = Review()
        string = "[Review] ({}) {}".format(rev.id, rev.__dict__)
        self.assertEqual(string, str(rev))

    def test_to_dict_contains_added_attributes(self):
        """method tests add attr"""
        rev = Review()
        rev.mid_name = "ALX"
        rev.num = 15
        self.assertEqual("ALX", rev.mid_name)
        self.assertIn("num", rev.to_dict())

    def test_to_dict_attrs_strs(self):
        """method tests type of instance of an object after calling to_dict"""
        rev = Review()
        newDict = rev.to_dict()
        self.assertEqual(str, type(newDict["id"]))
        self.assertEqual(str, type(newDict["updated_at"]))
        self.assertEqual(str, type(newDict["created_at"]))

    def test_save_updates_file(self):
        """method tests checks for class id into json file"""
        rev = Review()
        rev.save()
        rev_id = "Review." + rev.id
        with open("file.json", "r") as f:
            self.assertIn(rev_id, f.read())
