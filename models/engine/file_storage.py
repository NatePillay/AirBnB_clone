#!/usr/bin/python3
from json import dump, load
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
        objects = FileStorage.__objects
        dict_from_obj = {key: obj.to_dict() for key, obj in objects.items()}

        with open(FileStorage.__file_path, 'w') as file:
            dump(dict_from_obj, file)

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
