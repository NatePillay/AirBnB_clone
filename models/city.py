#!/usr/bin/python3
from models.base_model import BaseModel
'''class for city'''


class City(BaseModel):
    def __init__(self):
        self.state_id = ''
        self.name = ''
