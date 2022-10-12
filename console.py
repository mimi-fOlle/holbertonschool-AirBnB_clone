#!/usr/bin/python3
"""Program console.py that contains the entry point of the cmd interpreter"""
import cmd
import models
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

    def precmd(self, line):
        "Handles command errors"
        if len(line) > 0:
            args = line.split()
            command = args[0]
            if command == "create":
                if len(args) < 2:
                    print("** class name missing **")
                    return ""
                elif args[1] != "BaseModel":
                    print("** class doesn't exist **")
                    return ""
                return line

            elif command in ("show", "destroy"):
                if len(args) < 2:
                    print("** class name missing **")
                    return ""
                elif args[1] != "BaseModel":
                    print("** class doesn't exist **")
                    return ""
                elif len(args) < 3:
                    print("** instance id missing **")
                    return ""
                return line
        return line

    def do_create(self, arg):
        "Creates a new instance of BaseModel and saves it to the JSON file"
        inst = BaseModel()
        inst.save()
        print(inst.id)

    def do_show(self, arg):
        ("Prints the str representation of an instance based on class name "
         "and id")
        args = arg.split()
        id = args[1]
        insts = models.storage.all()
        key = f"BaseModel.{id}"

        if key in insts:
            print(insts[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        "Deletes an instance based on class name and id"
        args = arg.split()
        id = args[1]
        insts = models.storage.all()
        key = f"BaseModel.{id}"

        if key in insts:
            insts.pop(key)
            models.storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
