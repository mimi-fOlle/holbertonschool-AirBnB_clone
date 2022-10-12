#!/usr/bin/python3
"""Program console.py that contains the entry point of the cmd interpreter"""
import cmd
import ast
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
        if len(line.strip()) > 0:
            args = line.split()
            command = args[0]
            if command == "create":
                if len(args) < 2:
                    print("** class name missing **")
                    return ""
                elif args[1] not in models.classes:
                    print("** class doesn't exist **")
                    return ""
                return line

            elif command in ("show", "destroy", "update"):
                if len(args) < 2:
                    print("** class name missing **")
                    return ""
                elif args[1] not in models.classes:
                    print("** class doesn't exist **")
                    return ""
                elif len(args) < 3:
                    print("** instance id missing **")
                    return ""
                return line
        return line

    def do_create(self, arg):
        "Creates a new class instance and saves it to the JSON file"
        args = arg.split()
        classname = args[0]
        inst = models.classes[classname]()
        inst.save()
        print(inst.id)

    def do_show(self, arg):
        ("Prints the str representation of an instance based on class name "
         "and id")
        args = arg.split()
        classname = args[0]
        id = args[1]
        insts = models.storage.all()
        key = f"{classname}.{id}"

        if key in insts:
            print(insts[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        "Deletes an instance based on class name and id"
        args = arg.split()
        classname = args[0]
        id = args[1]
        insts = models.storage.all()
        key = f"{classname}.{id}"

        if key in insts:
            insts.pop(key)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        ("Updates an instance based on the class name and id "
         "by adding or updating attribute")
        args = arg.split()
        insts = models.storage.all()
        classname = args[0]
        id = args[1]
        key = f"{classname}.{id}"

        if key not in insts:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            attr_name = args[2]
            attr_value = args[3]
            attr_type = type(ast.literal_eval(attr_value))
            to_update = insts[key]

            if attr_type.__name__ != 'str':
                setattr(to_update, attr_name, attr_type(attr_value))
            else:
                setattr(to_update, attr_name, ast.literal_eval(attr_value))
            models.storage.save()

    def do_all(self, arg):
        ("Prints all string representations of all instances, "
         "based or not on class name")
        args = arg.split()
        insts = models.storage.all()
        if len(args) == 0:
            print([str(value) for value in insts.values()])
        else:
            to_print = [str(obj) for key, obj in insts.items()
                        if key.split('.')[0] == args[0]]
            if to_print:
                print(to_print)
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
