#!/usr/bin/python3
from json import dump, load
from models.base_model import BaseModel
from models.user import User

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
        key = '{} {}'.format(self.__class__.__name__, self.id)
        self.__obects[key] = obj

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
            with open(self.__file_path, 'r') as file:
                dict_from_json = load(file)
                for obj in dict_from_json.values():
                    self.new(eval(obj['__class__'])(**obj))
        except Exception:
            return
