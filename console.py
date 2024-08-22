#!/usr/bin/python3
""""Console Module"""

import cmd
from models import storage
from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, line):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """Create an object of any class"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = eval(class_name)()
            obj.save()
            print(obj.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Method to show an individual object.
        """
        args_list = args.split()
        class_name = args_list[0]
        class_id = args_list[1]

        if not class_name:
            print("** class name missing **")

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")

        if not class_id:
            print("** instance id missing **")

        key = f"{class_name}.{class_id}"

        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Deletes a specified object
        """
        args_list = args.split()
        class_name = args_list[0]
        class_id = args_list[1]

        if not class_name:
            print("** class name missing **")

        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")

        if not class_id:
            print("** instance id missing **")

        key = f"{class_name}.{class_id}"

        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
