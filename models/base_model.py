#!/usr/bin/python3
'''UUID for each request'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''create a new base model class 3
        attributes, taking no. of position and keyword args'''

        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        for key, value in kwargs.items():
            if key in ['created_as', 'updated_at']:
                self.__dict__[key] = datetime.fromisoformat(value)
            elif key != '__close__':
                self.__dict__[key] = value

    def __str__(self):
        ''' defines custom string representation of object'''
        return f'[{self.__class__.__name__}], ({self.id}], {self.__dict__}'

    def save(self):
        self.updated_as = datetiime.now()
        models.storage.save()

    def to_dict(self):
        '''method to convert an instance of
        BaseModel class into dict rep of object'''
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_idict
