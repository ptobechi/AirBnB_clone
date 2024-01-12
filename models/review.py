#!/usr/bin/python3

"""
airbnb clone review module that inherits from the basemodel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    a review calss

    Attributes:
        place_id
        user_id
        text
    """
    place_id = ""
    user_id = ""
    text = ""
