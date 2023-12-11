#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Defines  city class.'''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the City"""
        super().__init__(*args, **kwargs)
