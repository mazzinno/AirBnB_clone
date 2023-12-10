#!/usr/bin/python3
"""
Write a class that defines all common attributes/methods for other classes
"""
import json

class FileStorage:
    """
    class that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
