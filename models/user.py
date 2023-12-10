#!/usr/bin/python3
"""user module

This module represents the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User class

    Attributes:
        email (str): the user email
        password (str): the user password
        first_name (str): the user first name
        last_name (str): the user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
