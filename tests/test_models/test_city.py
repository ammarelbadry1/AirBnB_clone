#!/usr/bin/python3
"""Unittest module for City class"""

import models
from models.city import City
import unittest
from datetime import datetime


class TestCity_class(unittest.TestCase):
    """unittests for Amenity class"""

    def test_no_args_instantiates(self):
        """method tests instance with no args"""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """method tests instance stored in dict"""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """method check for id is public"""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_is_public_class_attr(self):
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_instant_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_args_unused(self):
        """method tests unused args"""
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_class_instances(self):
        """method that tests all class instances"""
        cy = City()

        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_str_method(self):
        """method test the str method has the correct output"""
        cy = City()
        string = "[City] ({}) {}".format(cy.id, cy.__dict__)
        self.assertEqual(string, str(cy))

    def test_to_dict_contains_added_attributes(self):
        """method tests add attr"""
        cy = City()
        cy.mid_name = "ALEX"
        cy.num = 15
        self.assertEqual("ALEX", cy.mid_name)
        self.assertIn("num", cy.to_dict())

    def test_to_dict_attrs_strs(self):
        """method tests type of instance of an object after calling to_dict"""
        cy = City()
        newDict = cy.to_dict()
        self.assertEqual(str, type(newDict["id"]))
        self.assertEqual(str, type(newDict["updated_at"]))
        self.assertEqual(str, type(newDict["created_at"]))

    def test_save_updates_file(self):
        """method tests checks for class id into json file"""
        cy = City()
        cy.save()
        cy_id = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cy_id, f.read())
