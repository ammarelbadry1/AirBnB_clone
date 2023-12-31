#!/usr/bin/python3
""" FileStorage class module"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = dict()
    __models = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
               }

    def all(self):
        """method returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """
        method sets in __objects the obj with key <obj class name>.id
        Args:
            obj: an object of class
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def destroy(self, key):
        """Deletes an object from __objects
        and save the changes to the JSON file"""
        FileStorage.__objects.pop(key)
        self.save()

    def update(self, key, obj):
        """Updates an object from __objects
        and save the changes to the JSON file"""
        FileStorage.__objects[key] = obj
        self.save()

    def save(self):
        """method that serializes __objects to the JSON file"""
        new_dict = FileStorage.__objects
        obj_dict = dict()
        for key in new_dict.keys():
            obj_dict[key] = new_dict[key].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """method that deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_obj = json.load(f)
                for val in json_obj.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(self.__models[class_name](**val))
        except FileNotFoundError:
            return
