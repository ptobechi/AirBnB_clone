#!/usr/bin/python3

"""
airbnb clone city module that inherits from the basemodel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    a city class

    Attributes:
        name
        state_if
    """
    name = ""
    state_id = ""
