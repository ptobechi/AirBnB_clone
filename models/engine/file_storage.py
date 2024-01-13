#!/usr/bin/python3
"""
a file storage module
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    a file storage class
    Attributes:
        __file_path: file storage location
        __objects: file storage format
    """
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def all(self, cls=None):
        if cls is not None:
            objects_of_cls = {key: obj for key, obj in self.__objects.items()
                              if type(obj).__name__ == cls}
            return objects_of_cls
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if exists(FileStorage.__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review

            FileStorage.classes.update({
                "BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review
            })
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in self.classes:
                        obj_class = self.classes[class_name]
                        obj = obj_class(**value)
                        self.__objects[key] = obj
