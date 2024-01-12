#!/usr/bin/python3

"""
A user module that inherits the basemodel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    A user class model
    Attributes:
        email: user email address
        password: user password
        first_name: user firsstname
        last_name: user lastname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
