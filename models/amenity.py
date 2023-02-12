#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''cass for Amenity'''
    def __init__(self):
        self.name = ''
