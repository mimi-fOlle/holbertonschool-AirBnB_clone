#!/usr/bin/python3
"""Program console.py that contains the entry point of the cmd interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class definition of the command intepreter"""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """
        A single EOF (character or EOF string written), like quit, exits the
        program
        """
        return True

    def do_quit(self, arg):
        "Exits the program"
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
