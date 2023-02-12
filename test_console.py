#!/usr/bin/python3
'''defines the console'''
import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt: '(hbnb)'

    def emtpyline(self):
        '''if empty line is passed do nothing'''
        pass

    def do_EOF(self, line):
        '''command to exit the program'''
        return True

    def do_quit(self, arg):
        ''' Quit command to exit the program'''
        return True

    def do_help(self, line):
        '''provide help for hbnb'''
        if line:
            '''user is asking for specific help commands'''
            try:
                help_func = getattr(self,f'help_{line}')
                help_func()
            except AttributeError:
                print(f"No help avaliable for '{line}'")
        else:
            '''general help required'''
            self.help.command()

    def do_create(class_name=None):
        '''implementing a create function'''
        if class_name = None:
            print("class name missing")
            return
        try:
            model = eval(class_name+ "()")
        except NameError:
            print("class doesn't exist")
            return
        model.id = 1
        model.save()
        print(model.id)

    def do_show(class_name=None, instance_id=None):
        '''implementing the show function'''
        if class_name = None:
            print("class name missing")
            return
        try:
            cls = eval(class_name)
        except NameError:
            print("class doesn't exist")
            return
        if not issubclass(cls, BaseModel):
            print("class doesn't exist")
            return

        if instance_id is None:
            print("instance id missing")
            return
        if instance_id not in cls.instances:
            print("no instance found")
            return
        instance = cls.instances[instance_id]
        print(instance)


        

    if __name__ == '__main__':
            HBNBCommand() the console
