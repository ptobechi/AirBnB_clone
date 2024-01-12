#!/usr/bin/python3

"""
airbnb clone place module that inherits from the basemodel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    a place calss

    Attributes:
        name
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
    longtitude = 0.0
    amenity_ids = []
