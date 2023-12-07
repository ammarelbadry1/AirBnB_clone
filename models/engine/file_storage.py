#!/usr/bin/python3
""" FileStorage class module"""

from models.base_model import BaseModel
import json


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """method returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """
        method sets in __objects the obj with key <obj class name>.id
        Args:
            obj: an object of class
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

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
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            return
