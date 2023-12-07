#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "

    def emptyline(self):
        print(end='')
    def do_greet(self, line):
        """print hello"""
        print("hello")

    def do_EOF(self, line):
        """exit the programm"""
        return True

    def do_quit(self, line):
        """exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
