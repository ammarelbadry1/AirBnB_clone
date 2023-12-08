#!/usr/bin/python3
"""console module/program

This module defines HBNBCommand child class
that inherits the command interpreter functionality
from the super class Cmd.
"""
import cmd
import re
import models


class HBNBCommand(cmd.Cmd):
    """Represent a HBNBCommand class

    Attributes:
        prompt (str): the string issued to solicit input
    """

    prompt = "(hbnb) \n"
    __available_models = ["BaseModel"]
    __models = {"BaseModel": models.base_model.BaseModel}

    # ----- Overwritten super class methods -----
    def emptyline(self):
        """Makes nothing when the input is empty line
        """
        pass

    # def precmd(self, line):
    #     print()
    #     return cmd.Cmd.precmd(self, line)

    # ----- Utils -----
    def parse_input(self, line):
        """Parses the input to arguments

        Args:
            line (str): the input to be parsed

        Return:
            a list of token strings
        """
        args = re.split(r'\s+|"([^"]*)"', line)
        words = []
        for arg in args:
            if arg == "" or arg is None:
                continue
            words.append(arg)
        return words

    def is_id_matched(self, id):
        """Checks if the id passed matches existent id

        Args:
            id (str): the id to be matched

        Return:
            True if matching, otherwise False
        """
        all_objs = models.storage.all()
        for obj in all_objs:
            tokens = obj.split('.')
            if id == tokens[1]:
                return True
        return False

    # ----- Basic console commands -----
    def do_create(self, line):
        """Creates a new instance of the class name passed
as an argument, if it exists, and saves it to the JSON file
and prints the created instance id"""

        args = self.parse_input(line)
        length = len(args)
        if length >= 1 and args[0] in self.__available_models:
            instance = self.__models[args[0]]()
            instance.save()
            print(instance.id)
        elif length >= 1:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
based on the class name and id"""
        args = self.parse_input(line)
        length = len(args)
        if (length >= 2
                and args[0] in self.__available_models
                and self.is_id_matched(args[1])):
            key = "{}.{}".format(args[0], args[1])
            all_objs = models.storage.all()
            obj = all_objs[key]
            print(obj)
        elif length >= 2 and args[0] in self.__available_models:
            print("** no instance found **")
        elif length >= 1 and args[0] in self.__available_models:
            print("** instance id missing **")
        elif length >= 1:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
(save the change into the JSON file)"""
        args = self.parse_input(line)
        length = len(args)
        if (length >= 2
                and args[0] in self.__available_models
                and self.is_id_matched(args[1])):
            key = "{}.{}".format(args[0], args[1])
            models.storage.destroy(key)
        elif length >= 2 and args[0] in self.__available_models:
            print("** no instance found **")
        elif length >= 1 and args[0] in self.__available_models:
            print("** instance id missing **")
        elif length >= 1:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """ Prints all string representation of all instances
based or not on the class name"""
        args = self.parse_input(line)
        length = len(args)
        all_objs = models.storage.all()
        objs_list = []
        if length >= 1 and args[0] in self.__available_models:
            for obj in all_objs.values():
                if args[0] == obj.__class__.__name__:
                    objs_list.append(str(obj))
            print(objs_list)
        elif length >= 1:
            print("** class doesn't exist **")
        else:
            for obj in all_objs.values():
                objs_list.append(str(obj))
            print(objs_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by
adding or updating attribute (save the change into the JSON file)"""
        args = self.parse_input(line)
        length = len(args)
        if (length >= 4
                and args[0] in self.__available_models
                and self.is_id_matched(args[1])):
            key = "{}.{}".format(args[0], args[1])
            all_objs = models.storage.all()
            obj = all_objs[key]
            obj.__dict__.update({args[2]: args[3]})
            print(obj.__dict__)
            models.storage.update(key, obj)
        elif (length >= 3
                and args[0] in self.__available_models
                and self.is_id_matched(args[1])):
            print("** value missing **")
        elif (length >= 2
                and args[0] in self.__available_models
                and self.is_id_matched(args[1])):
            print("** attribute name missing **")
        elif length >= 2 and args[0] in self.__available_models:
            print("** no instance found **")
        elif length >= 1 and args[0] in self.__available_models:
            print("** instance id missing **")
        elif length >= 1:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

# def destroy(self, key):
#     FileStorage.__objects.pop(key)
#     self.save()

# def update(self, key, obj):
#     FileStorage.__objects[key] = obj
#     self.save()
