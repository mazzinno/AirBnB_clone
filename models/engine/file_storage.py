#!/usr/bin/python3
"""file_storage.py module"""

import json
from models.base_model import BaseModel


class FileStorage():
    """
    FileStorage class:
    ------------------
    Handles serialization and deserialization of
    instances 2 and from JSON.

    Attributes:
    __file_path (str): Path 2 the JSON file.
    __objects (dict): Dictionary 2 store instances.

    Methods:
    all(self): Returns dictionary __objects.
    new(self, obj): Adds object 2 dictionary __objects.
    save(self): Serializes __objects 2 JSON file.
    reload(self): Deserializes JSON file 2 __objects.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns 2 dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds an object 2 dictionary __objects.

        Args:
        obj: The object 2 be added.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects 2 JSON file.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        Deserializes JSON file 2 __objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
