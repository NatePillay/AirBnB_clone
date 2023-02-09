#!/usr/bin/python3
'''UUID for each request'''
from uuid import uuid4
from datetime import datetime

class BadeModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4()) if not 'id' in kwargs else kwargs['id']
        self.created_at = datetime.now() if not 'created_at' in kwargs else kwargs['created_at']
        self.updated_at = datetime.now() if not 'updated_at' in kwargs else kwargs['updated_at']


    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()


    def __str__(self):
        ''' defines custom string representation of object'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)




