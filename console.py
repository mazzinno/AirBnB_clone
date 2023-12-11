#!/usr/bin/python3
""" Defines entry point of the command interpreter."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [index.strip(",") for index in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [index.strip(",") for index in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [index.strip(",") for index in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    Implements the class HBNBCommand.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            }

    def default(self, arg):
        """ Improves the default cmd. """
        argdict = {
                "show": self.do_show,
                "destroy": self.do_destroy,
                "all": self.do_all,
                "update": self.do_update,
                "count": self.do_count
                }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])

            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]

                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, args):
        """ Quit command to exit. """
        return True

    def do_EOF(self, arg):
        """ EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """ Nothing done when recieving an empty line"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it."""
        argl = parse(arg)

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        argl = parse(arg)
        objd = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objd:
            print("** no instance found **")
        else:
            print(objd["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id."""
        argl = parse(arg)
        objd = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objd.keys():
            print("** no instance found **")
        else:
            del objd["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based.
        """
        argl = parse(arg)

        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []

            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        argl = parse(arg)
        objd = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False

        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        if len(argl) == 1:
            print("** instance id missing **")
            return False

        if "{}.{}".format(argl[0], argl[1]) not in objd.keys():
            print("** no instance found **")
            return False

        if len(argl) == 2:
            print("** attribute name missing **")
            return False

        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objd["{}.{}".format(argl[0], argl[1])]

            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objd["{}.{}".format(argl[0], argl[1])]

            for index, jndex in eval(argl[2]).items():
                if (index in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[index]) in
                        {str, int, float}):
                    valtype = type(obj.__class__.__dict__[index])
                    obj.__dict__[jndex] = valtype(jndex)
                else:
                    obj.__dict__[index] = jndex
        storage.save()

    def do_count(self, arg):
        """ Retrieve the number of instances of a class."""
        argl = parse(arg)
        count = 0

        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
