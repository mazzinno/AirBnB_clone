#!/usr/bin/python3
'''Defines Review class.'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Represents Review class.'''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
