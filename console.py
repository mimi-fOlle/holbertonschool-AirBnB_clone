#!/usr/bin/python3
"""Program console.py that contains the entry point of the cmd interpreter"""


import cmd

class HBNBCommand(cmd.Cmd):
    """class definition """
    
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print("Exit\n")

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
