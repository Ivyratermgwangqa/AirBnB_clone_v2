#!/usr/bin/python3
"""This is the console for AirBnB"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "City", "State", "Amenity", "Place", "Review"}

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it"""
        try:
            if not line:
                raise SyntaxError()

            class_name, *args = line.split()

            kwargs = {}
            for arg in args:
                key, val = arg.split("=")
                val = val.strip('"').replace("_", " ") if val[0] == '"' else eval(val)
                kwargs[key] = val

            obj = globals()[class_name](**kwargs) if kwargs else globals()[class_name]()
            storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        try:
            if not line:
                raise SyntaxError()

            class_name, obj_id = line.split()

            if class_name not in self.__classes:
                raise NameError()

            key = f"{class_name}.{obj_id}"
            obj = storage.all().get(key)

            if not obj:
                raise KeyError()

            print(obj)

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        try:
            if not line:
                raise SyntaxError()

            class_name, obj_id = line.split()

            if class_name not in self.__classes:
                raise NameError()

            key = f"{class_name}.{obj_id}"
            obj_dict = storage.all()

            if key not in obj_dict:
                raise KeyError()

            del obj_dict[key]
            storage.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        try:
            if not line:
                obj_dict = storage.all()
                print([str(obj) for obj in obj_dict.values()])
                return

            class_name = line.split()[0]
            if class_name not in self.__classes:
                raise NameError()

            obj_dict = storage.all(eval(class_name))
            print([str(obj) for obj in obj_dict.values()])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance by adding or updating attribute"""
        try:
            if not line:
                raise SyntaxError()

            my_list = split(line, " ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = f"{my_list[0]}.{my_list[1]}"
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()

            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """Count the number of instances of a class"""
        counter = 0
        try:
            class_name = line.split()[0]

            if class_name not in self.__classes:
                raise NameError()

            objects = storage.all()
            counter = sum(1 for key in objects if key.split('.')[0] == class_name)

            print(counter)

        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """Strips the argument and returns a string of the command"""
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """Retrieve all instances of a class and retrieve the number of instances"""
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
