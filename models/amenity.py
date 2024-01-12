#!/usr/bin/python3

"""
airbnb clone amenity module that inherits from the basemodel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    a amenity calss

    Attributes:
        name
    """
    name = ""
