#!/usr/bin/python3
"""test_base_model module

This module apply unittests on base model
"""
import unittest, datetime, uuid, time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines the unittests of the BaseModel class"""

    def test_init(self):
        """Tests the initialization of the BaseModel objects"""
        time_before = datetime.datetime.now()
        time.sleep(0.2)
        obj1 = BaseModel()
        time.sleep(0.2)
        time_after = datetime.datetime.now()
        obj2 = BaseModel()
        obj3 = BaseModel()
        obj3.email = "foo@mail.co"
        obj3.password = "123"
        obj4 = BaseModel(**obj3.to_dict())


        # test the object
        self.assertIsInstance(obj1, BaseModel)
        self.assertIsNot(obj3, obj4)
        self.assertEqual(obj3.__dict__, obj4.__dict__)

        # test the object id
        self.assertTrue(hasattr(obj1, "id"))
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertIsInstance(obj1.id, str)

        # test the object created_at attribute
        self.assertTrue(hasattr(obj1, "created_at"))
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertGreater(obj1.created_at, time_before)
        self.assertLess(obj1.created_at, time_after)
        self.assertIsInstance(obj1.created_at, datetime.datetime)

        # test the object updated_at attribute
        self.assertTrue(hasattr(obj1, "updated_at"))
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
        self.assertGreater(obj1.updated_at, time_before)
        self.assertLess(obj1.updated_at, time_after)
        self.assertIsInstance(obj1.updated_at, datetime.datetime)

    def test_str(self):
        """Tests the string representation of the BaseModel objects"""
        obj = BaseModel()
        obj_str = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id, obj.__dict__)

        self.assertEqual(str(obj), obj_str)

    def test_save(self):
        """Tests the save method of the BaseModel objects"""
        obj = BaseModel()

        time_before_save = obj.updated_at
        time_before = datetime.datetime.now()
        time.sleep(0.2)
        obj.save()
        time.sleep(0.2)
        time_after = datetime.datetime.now()

        self.assertNotEqual(obj.updated_at, time_before_save)
        self.assertGreater(obj.updated_at, time_before)
        self.assertLess(obj.updated_at, time_after)

    def test_to_dict(self):
        """Tests the to_dict method of the BaseModel objects"""
        obj1 = BaseModel()
        obj1.email = "foo@mail.co"
        obj1.password = "123"
        obj1_dict = obj1.to_dict()
        obj2 = BaseModel(**obj1_dict)
        obj2_dict = obj2.to_dict()

        # test the method return type
        self.assertIsInstance(obj1_dict, dict)

        # test the __class__ attribute
        self.assertIn("__class__", obj1_dict)
        self.assertEqual(obj1_dict["__class__"], obj1.__class__.__name__)

        # test the time format
        obj_created_at = obj1.created_at.isoformat()
        obj_updated_at = obj1.updated_at.isoformat()
        self.assertIn("created_at", obj1_dict)
        self.assertIn("updated_at", obj1_dict)
        self.assertEqual(obj1_dict["created_at"], obj_created_at)
        self.assertEqual(obj1_dict["updated_at"], obj_updated_at)

        # test the existence of the rest obj attributes
        del obj1.created_at, obj1.updated_at
        for key in obj1.__dict__:
            self.assertIn(key, obj1_dict)
            self.assertEqual(obj1.__dict__[key], obj1_dict[key])

        # test to_dict with kwargs
        self.assertEqual(obj1_dict, obj2_dict)
