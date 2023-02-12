#!/usr/bin/python3
from models.base_model import BaseModel
'''creating attributes for the user '''

class User(BaseModel):
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
