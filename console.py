#!/usr/bin/python3
"""Program console.py that contains the entry point of the cmd interpreter"""
import cmd
from models.base_model import BaseModel


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

    def do_create(self, arg):
        "Creates a new instance of BaseModel and saves it to the JSON file"
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            inst.save()
            print(inst.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
