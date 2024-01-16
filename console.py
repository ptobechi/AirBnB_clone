#!/usr/bin/python3

"""
a python command line interpreter (console/terminal) module
"""

import cmd
import json
import re

import models
from models import BaseModel, User, State, \
    City, Amenity, Place, Review


def isfloat(s):
    '''Checks if a string is a decimal'''
    try:
        float(s)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = '(hbnb) '
    model_list = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', "Place", "Review"
                  ]
    queries = ['all', 'count', 'show', 'destroy', 'update']

    @classmethod
    def handle_errors(cls, arg: str, **kwarg):
        '''Error Handler for all commands'''

        if "all" in kwarg.values():
            if not arg:
                return False

        if not arg:
            print("** class name missing **")
            return True
        else:
            arg = arg.split(" ")

        n = len(arg)

        if n < 1:
            print("** class name missing **")
            return True

        if arg[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return True

        if 'command' not in kwarg:
            return False

        for _, arg in kwarg.items():
            if arg in ['create', 'show', 'destroy']:
                if n < 2:
                    print("** instance id missing **")
                    return True
            elif arg in ['update']:
                if n < 2:
                    print("** instance id missing **")
                    return True
                elif n < 3:
                    print("** attribute name missing **")
                    return True
                elif n < 4:
                    print("** value missing **")
                    return True
                elif n == 4 and arg[2] == "":
                    print("** attribute name missing **")
                    return True

        return False

    def do_quit(self, arg: str):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg: str):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        return False

    def do_create(self, arg: str):
        """Creates a new instance of BaseModel"""
        if HBNBCommand.handle_errors(arg):
            return

        arg = arg.split(" ")
        obj = eval(arg[0])()
        obj.save()
        print(obj.id)

    def do_show(self, arg: str):
        """Prints the string representation of an instance"""
        if HBNBCommand.handle_errors(arg, command='show'):
            return

        arg = arg.split(" ")
        objects = models.storage.all()
        key = ".".join(arg)
        obj = objects.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg: str):
        """Deletes an instance based on the class name and id"""
        if HBNBCommand.handle_errors(arg, command='destroy'):
            return

        arg = arg.split(" ")
        objects = models.storage.all()
        key = ".".join(arg)

        delete = False
        if key in objects and models.storage.delete(objects[key]):
            pass
        else:
            print("** no instance found **")

    def do_all(self, arg: str):
        """Prints all string representation of all instances"""
        if HBNBCommand.handle_errors(arg, command='all'):
            return

        arg = arg.split(" ")

        objects = models.storage.all()

        if arg[0] == "":
            for obj in objects.values():
                print(obj)

        else:
            for key in objects:
                k = key.split(".")
                if k[0] == arg[0]:
                    print(objects[key])

    def do_update(self, arg: str):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if HBNBCommand.handle_errors(arg, command='update'):
            return

        arg = arg.split(" ")
        attr_name = arg[2]
        attr_value = str(arg[3])
        if attr_value[0] == "\"" or attr_value[0] == "'":
            attr_value = attr_value[1:-1]
        if attr_value.isdigit():
            attr_value = int(attr_value)
        elif isfloat(attr_value):
            attr_value = float(attr_value)

        objects = models.storage.all()
        key = ".".join(arg[:2])

        obj = objects.get(key)
        if obj:
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")

    def do_count(self, arg: str):
        '''
        counts all string representation of all instances based
        or not on the class name.

        Usage: count <class_name>
               <class name>.count()
        '''

        if HBNBCommand.handle_errors(arg):
            return

        arg = arg.split(" ")
        objects = models.storage.all()
        _all = []

        for k, v in objects.items():
            key = k.split(".")
            if key[0] == arg[0]:
                _all.append(str(v))

        print(len(_all))

    def onecmd(self, arg: str):
        pattern = re.compile(
            r"(\w+)\.(\w+)\(((\"[\w|-]+\"),?\s?(\"\w+\")?,\
            ?\s?(\"?[\w\.]+\"?)?)?\)"
        )

        pattern2 = re.compile(
            r"(\w+)\.(\w+)\((\"[\w-]+\"),\s?\{(.+)\}\)"
        )

        match = pattern.search(arg)
        match2 = pattern2.search(arg)
        if match:
            self.handle_match(match)
        elif match2:
            self.handle_match2(match2)
        elif arg == "quit":
            return self.do_quit(arg)
        elif arg == "EOF":
            return self.do_EOF(arg)
        else:
            cmd.Cmd.onecmd(self, arg)

    def handle_match(self, match: re.Match):
        groups = match.groups()
        if groups[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return
        if groups[1] not in HBNBCommand.queries:
            print(f"** unknown command: '{groups[1]}' **")
            return
        if groups[1] == 'all':
            arg = f"{groups[1]} {groups[0]}"
            cmd.Cmd.onecmd(self, arg)
            return
        elif groups[1] == 'count':
            arg = f"{groups[1]} {groups[0]}"
            cmd.Cmd.onecmd(self, arg)
            return
        elif groups[1] == 'show':
            if groups[3]:
                id = groups[3][1:-1]
            else:
                id = ""
            arg = f"{groups[1]} {groups[0]} {id}"
            cmd.Cmd.onecmd(self, arg)
            return
        elif groups[1] == "destroy":
            if groups[3]:
                id = groups[3][1:-1]
            else:
                id = ""
            arg = f"{groups[1]} {groups[0]} {id}"
            cmd.Cmd.onecmd(self, arg)
            return
        elif groups[1] == 'update':
            if groups[3]:
                id = groups[3][1:-1]
            else:
                id = ""
            if groups[4]:
                attr_name = groups[4][1:-1]
            else:
                attr_name = ""

            if not groups[5]:
                attr_value = ""
            elif "\"" not in groups[5]:
                attr_value = groups[5]
            elif groups[5]:
                attr_value = groups[5][1:-1]

            arg = f"{groups[1]} {groups[0]} {id} {attr_name} {attr_value}"
            cmd.Cmd.onecmd(self, arg)
            return

    def handle_match2(self, match: re.Match):
        groups1 = match.groups()
        if groups1[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return
        if groups1[1] != 'update':
            print(f"** This only works for update command **")
            return

        if groups1[3]:
            pattern = re.compile(
                r"[\'\"](\w+)[\'\"]\s?:\s?[\'\"]?([\w\.]+)[\'\"]?,?\s?"
            )
            match = pattern.finditer(groups1[3])
            results = []
            for m in match:
                for part in m.groups():
                    results.append(part)

        if not results or len(results) % 2 != 0:
            print("** something went wrong in the dictionary argument **")
            return
        else:
            class_name = groups1[0]
            query = groups1[1]
            id = groups1[2]
            if id[0] == "\"" or id[-1] == "\"":
                id = id[1:-1]

            for i in range(0, len(results), 2):
                attr_name = results[i]
                attr_value = results[i+1]
                arg = f"{query} {class_name} {id} {attr_name} {attr_value}"
                cmd.Cmd.onecmd(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
