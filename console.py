#!/usr/bin/python3
'''
Command Interpreter
'''
import cmd
import shlex
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''command line class'''
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, args):
        '''
        Creating a new instance of BaseModel, save it, and print the id
        '''
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0] + '()')
            models.storage.save()
            print(new_instance.id)

    def do_show(self, args):
        '''
        Printing the string representation of a specific instance
        '''
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj_dict = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj_dict:
                print(obj_dict[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        '''
        Deleting an instance
        '''
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects:
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        '''
        Printing a string representation of all instances
        '''
        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        '''
        Update an instance
        '''
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """
        Checking if stdin user typed class name and id
        """
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """
        Checking class id
        """
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """
        Finding the name class
        """
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        '''
        Quiting command to exit the program
        '''
        return True

    def do_EOF(self, args):
        '''
        Handles end of file
        '''
        return True

    def emptyline(self):
        '''
        Don't execute anything when the user presses
        enter with an empty line
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
