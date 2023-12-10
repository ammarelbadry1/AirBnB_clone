#!/usr/bin/python3
"""BaseModel class Module"""
import models
import uuid
from datetime import datetime


time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class"""

    def __init__(self, *args, **kwargs):
        """
        Initialization method for BaseModel class.
        Args:
            *args: unused
            **kwargs: a key and value of a dictionry attribute
        """
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, time_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, time_format)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation method of BaseModel class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        method updates public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        method returns a dictionary containing all keys/values
        of __dict__ of an instance
        """
        newDict = self.__dict__.copy()
        newDict["__class__"] = self.__class__.__name__
        if "created_at" in newDict:
            newDict["created_at"] = newDict["created_at"].strftime(time_format)
        if "updated_at" in newDict:
            newDict["updated_at"] = newDict["updated_at"].strftime(time_format)
        return (newDict)
