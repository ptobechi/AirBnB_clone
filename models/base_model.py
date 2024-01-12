#!/usr/bin/python3
"""
A base model module for an airbnb clone
"""
import models
import uuid
from datetime import datetime

class BaseModel:
    """
    Base model class for the airbnb clone project
    """

    def __init__(self, *args, **kwargs):
        """
        Class model constructor function
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            models.engine.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value,
                                '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)

            # set class id
            self.id = kwargs.get('id', str(uuid.uuid4()))

            # set time when the instance of the class was created
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()

            # update to currenct time the class was updated after creation
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        models.engine.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                    self.__dict__)
