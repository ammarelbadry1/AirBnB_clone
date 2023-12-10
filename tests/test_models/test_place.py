#!/usr/bin/python3
"""Unittest module for Place class"""

import models
from models.place import Place
import unittest
from datetime import datetime


class TestPlace_class(unittest.TestCase):
    """unittests for Place class"""

    def test_no_args_instantiates(self):
        """method tests instance with no args"""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """method tests instance stored in dict"""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """method check for id is public"""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public(self):
        """method checks for created_at is public"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_name_is_public_class_attr(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_instant_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_args_unused(self):
        """method tests unused args"""
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_class_instances(self):
        """method that tests all class instances"""
        pl = Place()

        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_str_method(self):
        """method test the str method has the correct output"""
        pl = Place()
        string = "[Place] ({}) {}".format(pl.id, pl.__dict__)
        self.assertEqual(string, str(pl))

    def test_to_dict_contains_added_attributes(self):
        """method tests add attr"""
        pl = Place()
        pl.mid_name = "ALX"
        pl.num = 15
        self.assertEqual("ALX", pl.mid_name)
        self.assertIn("num", pl.to_dict())

    def test_to_dict_attrs_strs(self):
        """method tests type of instance of an object after calling to_dict"""
        pl = Place()
        newDict = pl.to_dict()
        self.assertEqual(str, type(newDict["id"]))
        self.assertEqual(str, type(newDict["updated_at"]))
        self.assertEqual(str, type(newDict["created_at"]))

    def test_save_updates_file(self):
        """method tests checks for class id into json file"""
        pl = Place()
        pl.save()
        pl_id = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(pl_id, f.read())
