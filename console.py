#!/usr/bin/python3
"""console module/program

This module represents HBNBCommand child class
that inherits the command interpreter functionality
from the super class Cmd.
"""
import cmd
import re
import models


class HBNBCommand(cmd.Cmd):
    """Defines a HBNBCommand class

    Attributes:
        prompt (str): the string issued to solicit input
        __available_models (list): the list of available models
        __models (dict): the dictionary of available models
    """

    prompt = "(hbnb) \n"
    __models = {
                    "BaseModel": models.base_model.BaseModel,
                    "User": models.user.User,
                    "State": models.state.State,
                    "City": models.city.City,
                    "Amenity": models.amenity.Amenity,
                    "Place": models.place.Place,
                    "Review": models.review.Review
               }
    __available_models = __models.keys()

    # ----- Overwritten super class methods -----
    def emptyline(self):
        """Makes nothing when the input is empty line
        """
        pass

    def onecmd(self, line):
        """Defines what to do with the input command
        """
        if len(line.split(".")) == 2:
            class_name, method = line.split(".")
            tokens = re.split(r'\(|"([^"]*)"|,', method)
            method_tokens = []
            for token in tokens:
                if (token == ""
                        or token == " "
                        or token == ")"
                        or token is None):
                    continue
                method_tokens.append(token)
            input_line = ""
            input_line += class_name + " "
            for i in range(1, len(method_tokens)):
                input_line += method_tokens[i] + " "
            match method_tokens[0]:
                case "all":
                    self.do_all(input_line)
                case "show":
                    self.do_show(input_line)
                case "destroy":
                    self.do_destroy(input_line)
                case "update":  # not fully handled
                    self.do_update(input_line)
                case "count":
                    objs = models.storage.all()
                    count = 0
                    for obj in objs.values():
                        if class_name == obj.__class__.__name__:
                            count += 1
                    print(count)

        else:
            return super().onecmd(line)

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
