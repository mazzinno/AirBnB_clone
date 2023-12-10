#!/usr/bin/python3
""" Defines all common attributes/methods."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Represents the BaseModel of the AirBnB project. """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel.

        Args:
            *args (any): Won't be used.
            **kwargs (dict): Key/Value pairsof the attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for index, jndex in kwargs.items():
                if index == "created_at" or index == "updated_at":
                    self.__dict__[index] = datetime.strptime(jndex, timeformat)
                else:
                    self.__dict__[index] = jndex
        else:
            models.storage.new(self)

    def __str__(self):
        """ Return the print/str representation the BaseModel instance. """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()

        return rdict
