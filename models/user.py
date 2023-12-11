#!/usr/bin/python3
'''Inherits from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Defines class User.'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
