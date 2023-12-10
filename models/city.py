#!/usr/bin/python3
"""city module

This module represents the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the City class

    Attributes:
        state_id (str): the id of the state to which the city belong
        name (str): the name of the city
    """

    state_id = ""
    name = ""
