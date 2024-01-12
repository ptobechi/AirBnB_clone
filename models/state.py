#!/usr/bin/python3

"""
airbnb clone state module that inherits from the basemodel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    a state calss

    Attributes:
        name
    """
    name = ""
