#!/usr/bin/python3
"""
A base model module for an airbnb clone
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base model class for the airbnb clone project
    """

    def __init__(self, *args, **kwargs):
        """
        Class model constructor function
        initialize instance for the model
        """
        if kwargs:
            for name, attr in kwargs.items():
                if name != '__class__':
                    if name not in ['created_at', 'updated_at']:
                        self.__setattr__(name, attr)
                    else:
                        self.__setattr__(name, datetime.fromisoformat(attr))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        to_dict = {}
        for key, value in self.__dict__.items():
            to_dict[key] = value

        to_dict['__class__'] = self.__class__.__name__

        to_dict['created_at'] = self.created_at.\
            strftime("%Y-%m-%dT%H:%M:%S.%f")

        to_dict['updated_at'] = self.updated_at.\
            strftime("%Y-%m-%dT%H:%M:%S.%f")

        return to_dict

    def __str__(self):
        """
        Should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
