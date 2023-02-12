#!/usr/bin/python3
from models.base_model import BaseModel
'''creating attributes for the user '''


class User(BaseModel):
    '''class for user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
