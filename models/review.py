#!/usr/bin/python3
"""review module

This module represents the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class

    Attributes:
        place_id (str): the id of the place to which the review belong
        user_id (str): the id of the user to which the review belong
        text (str): the content of the review
    """

    place_id = ""
    user_id = ""
    name = ""
