#!/usr/bin/python3
"""console module/program

This module defines HBNBCommand child class
that inherits the command interpreter functionality
from the super class Cmd.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Represent a HBNBCommand class

    Attributes:
        prompt (str): the string issued to solicit input
    """

    prompt = "(hbnb) "

    # ----- Overwritten super class methods -----
    def emptyline(self):
        """Makes nothing when the input is empty line
        """
        pass

    def postloop(self):
        """Prints a new line when the cmdloop return
        """
        print()

    # ----- Basic console commands -----
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
