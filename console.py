#!/usr/bin/python3

"""
a python command line interpreter (console/terminal) module
"""

import cmd
import shlex
from models.engine import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        all_objs = []
        if not args:
            for obj in storage.all().values():
                all_objs.append(str(obj))
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        else:
            # Use the <class name>.all() syntax to retrieve all instances
            all_objs = [str(obj) for obj in
                        storage.classes[args[0]].all().values()]
        print(all_objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif args[2] == "id" or args[2] == "created_at" or \
                    args[2] == "updated_at":
                print("** cannot update id, created_at, or updated_at **")
            else:
                obj = all_objs[key]
                try:
                    # Convert the value to the attribute type
                    value = type(getattr(obj, args[2]))(args[3])
                    setattr(obj, args[2], value)
                    obj.save()
                except ValueError:
                    print("** invalid value for attribute **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
