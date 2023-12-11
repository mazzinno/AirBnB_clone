#!/usr/bin/python3
""" Defines FileStorage class. """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Store all objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key<obj class name>.id."""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file."""
        obj_dict = FileStorage.__objects
        objd = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as myfile:
            json.dump(objd, myfile)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as myfile:
                objdict = json.load(myfile)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
