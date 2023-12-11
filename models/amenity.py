#!/usr/bin/python3
'''The `amenity` module
It defines one class, `Amenity(),
which sub-classes the `BaseModel()` class.
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''An amenity provided by a place/house.'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
