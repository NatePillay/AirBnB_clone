#!/usr/bin/python3
from models.base_model import BaseModel
'''class for review page'''

class Review(BaseModel):
    def __init__(self):
        self.place_id = ''
        self.user_id = ''
        self.text = ''
