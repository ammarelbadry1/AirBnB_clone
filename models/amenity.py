#!/usr/bin/python3
"""amenity module

This module represents the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the Amenity class

    Attributes:
        name (str): the name of the amenity
    """

    name = ""
