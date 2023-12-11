#!/usr/bin/python3
'''Defines the state class.'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Represents class State'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
