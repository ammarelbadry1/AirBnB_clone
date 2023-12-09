#!/usr/bin/python3
"""place module

This module represents the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the Place class

    Attributes:
        city_id (str): the id of the city to which the place belong
        user_id (str): the id of the user to which the place belong
        name (str): the name of the place
        description (str): the description of the place
        number_rooms (int): the rooms count
        number_bathrooms (int): the bathrooms count
        max_guest (int): maximum number of guests
        price_by_night (int): the price by night
        latitude (float): the place latitude (position attribute)
        longitude (float): the place longitude (position attribute)
        amenity_ids (list): the list of facilities and services ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
