#!/usr/bin/python3
"""
Module contains storage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns objects"""
        return self.__objects

    def new(self, obj):
        """adds obj to dict with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes objects to the json file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w+", encoding="utf-8") as myfile:
            str_rep = json.dumps(obj_dict)
            myfile.write(str_rep)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as myfile:
                str_rep = myfile.read()
                objects_dict = json.loads(str_rep)
                classes = {"User": User, "BaseModel": BaseModel,
                           "State": State, "City": City, "Amenity": Amenity,
                           "Place": Place, "Review": Review}
                for key in objects_dict:
                    """objects_dict[key] -> a dictionary ->
                    dictionary[__class__name]"""
                    dictionary = objects_dict[key]
                    cls = dictionary["__class__"]
                    self.__objects[key] = classes[cls](**objects_dict[key])
        except Exception:
            pass
