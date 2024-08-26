#!/usr/bin/python3
""""Console Module"""

import cmd
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = "(hbnb)"
    classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
                  }

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
            # obj = eval(class_name)()
            obj = HBNBCommand.classes[class_name]()  # safer than eval
            obj.save()
            print(obj.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Method to show an individual object.
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_id = args_list[1]
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
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_id = args_list[1]
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

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        if not args:
            new_list = [str(obj) for obj in storage.all().values()]
        else:
            # Remove possible trailing args
            args = args.split()[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            new_list = [str(v) for k, v in storage.all().items()
                        if k.split(".")[0] == args]

        print(new_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_update(self, args):
        """Updates a certain object with new information"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        class_name = args_list[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        if len(args_list) < 4:
            print("** value missing **")
            return

        class_id = args_list[1]
        key = f"{class_name}.{class_id}"

        if key not in storage.all().keys():
            print("** no instance found **")
        else:
            attribute_name = args_list[2]
            attribute_value = args_list[3]

            # Finding attribute type (casted).
            try:
                arg_type = type(ast.literal_eval(attribute_value))
            except (ValueError, SyntaxError):
                arg_type = str  # Fallback to string if eval fails

            attribute_value = attribute_value.strip('"').strip("'")
            setattr(storage.all()[key],
                    attribute_name,
                    arg_type(attribute_value)
                    )
            storage.all()[key].save()

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
