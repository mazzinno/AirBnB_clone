#!/usr/bin/python3
""" Inherits from the BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines class User.
    last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
