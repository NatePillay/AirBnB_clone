#!/usr/bin/python3
import json
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''Defines file storage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary of all created objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''set an object in the dictionary to a key =
        string rep of object class name cncate with ID'''
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        '''serializing obects into JSON'''
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        '''deserializing JSON data into objects
        try block used to handle exceptions
        eval takes string argument and returns obj'''
        try:
            with open(FileStorage.__file_path) as file:
                dict_from_json = load(file)
                for obj in dict_from_json.values():
                    self.new(eval(obj['__class__'])(**obj))
        except Exception:
            return
