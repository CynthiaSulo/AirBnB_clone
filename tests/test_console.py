#!/usr/bin/python3
"""
Contains class TestConsole.
"""
import unittest
import cmd
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os
import json


class TestHBNBCommand(unittest.TestCase):
    """
    Contains tests for console.
    """
    def setUp(self):
        """allocating resources"""
        models.storage._FileStorage__objects = {}


    def test_do_EOF(self):
        """tests do_EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            output = HBNBCommand().onecmd(f"EOF")
            self.assertTrue(output)

    def test_do_quit(self):
        """tests do_quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            output = HBNBCommand().onecmd(f"quit")
            self.assertTrue(output)

    def test_help(self):
        """help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help")
            li1 = "Documented commands (type help <topic>):"
            li2 = "========================================"
            li3 = "EOF  all  count  create  destroy  help  quit  show  update"
            expected = li1 + '\n' + li2 + '\n' + li3
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_help(self):
        """help help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help help")
            expected1 = 'List available commands with "help" '
            expected2 = 'or detailed help with "help cmd".'
            expected = expected1 + expected2
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_eof(self):
        """help eof"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help EOF")
            expected = "quit the program"
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_quit(self):
        """help quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help quit")
            expected = "quit the program"
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_all(self):
        """help all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help all")
            li1 = "Prints all string representation of"
            li2 = "        all instances based or not on the class name"
            expected = li1 + '\n' + li2
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_count(self):
        """help count"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help count")
            expected = "Retrieve the number of instances of a class."
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_create(self):
        """help create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help create")
            expected = "creates a new instance of BaseModel"
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_destroy(self):
        """help destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help destroy")
            li1 = "Deletes an instance based on the"
            li2 = "        class name and id"
            expected = li1 + '\n' + li2
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_help_show(self):
        """help show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"help show")
            li1 = "Prints the str rep of an instance based"
            li2 = "        on the class name and id"
            expected = li1 + '\n' + li2
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Base(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Base2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_User(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_User2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Amen(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Amen2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_City(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_City2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Place(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Place2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Review(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_Review2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_State(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_State2(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            dictionary = models.storage.all()
            for key, value in dictionary.items():
                expected = value.id
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_create_arg1(self):
        """tests do_create"""
        with patch('sys.stdout', new=StringIO()) as f1:
            HBNBCommand().onecmd(f"create")
            output1 = f1.getvalue().strip()
            expected_msg1 = "** class name missing **"
            self.assertEqual(expected_msg1, output1)

    def test_do_create_arg2(self):
        with patch('sys.stdout', new=StringIO()) as f2:
            cls_name = "MyModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            output2 = f2.getvalue().strip()
            expected_msg2 = "** class doesn't exist **"
            self.assertEqual(expected_msg2, output2)

    def test_do_count_empty(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            self.assertEqual(expected_count, int(output))

    def test_do_count_Base(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Base2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_User(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_User2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Amen(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Amen2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_City(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_City2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Place(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Place2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Review(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_Review2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_State(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            HBNBCommand().onecmd(f"count {cls_name}")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_count_State2(self):
        """tests do_count"""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"{cls_name}.create()")
            HBNBCommand().onecmd(f"{cls_name}.count()")
            dictionary = models.storage.all()
            counter = 0
            for key in dictionary:
                if dictionary[key].__class__.__name__ == cls_name:
                    counter += 1
            expected_count = counter
            output = f.getvalue().strip()
            output_full = output.split('\n')
            output_count = int(output_full[-1])
            self.assertEqual(expected_count, output_count)

    def test_do_show_empty(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "City"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_arg1(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f1:
            HBNBCommand().onecmd(f"show")
            output1 = f1.getvalue().strip()
            expected_msg1 = "** class name missing **"
            self.assertEqual(expected_msg1, output1)

    def test_do_show_arg2(self):
        """test do_show"""
        with patch('sys.stdout', new=StringIO()) as f2:
            cls_name = "MyModel"
            HBNBCommand().onecmd(f"show {cls_name}")
            dictionary = models.storage.all()
            output2 = f2.getvalue().strip()
            expected_msg2 = "** class doesn't exist **"
            self.assertEqual(expected_msg2, output2)

    def test_do_show_arg3(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f3:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"show {cls_name}")
            dictionary = models.storage.all()
            output3 = f3.getvalue().strip()
            expected_msg3 = "** instance id missing **"
            self.assertEqual(expected_msg3, output3)

    def test_do_show_arg4(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f4:
            cls_name = "Place"
            HBNBCommand().onecmd(f"show {cls_name} My_First_Model")
            output4 = f4.getvalue().strip()
            expected_msg4 = "** no instance found **"
            self.assertEqual(expected_msg4, output4)

    def test_do_show_Base(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "BaseModel"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Base2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "BaseModel"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_User(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "User"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_User2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "User"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Amen(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Amenity"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Amen2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Amenity"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_City(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "City"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_City2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "City"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Place(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Place"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Place2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Place"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Review(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Review"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_Review2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "Review"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_State(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "State"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} {str(value)}"
                HBNBCommand().onecmd(f"create {cls_name}")
                HBNBCommand().onecmd(f"show {cls_name} {cls_id}")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_show_State2(self):
        """tests do_show"""
        with patch('sys.stdout', new=StringIO()) as f:
            dictionary = models.storage.all()
            cls_name = "State"
            expected = ""
            for key, value in dictionary.items():
                if key.split('.')[0] == cls_name:
                    cls_id = value.id
                    expected = f"{cls_name} {cls_id} str({value})"
                HBNBCommand().onecmd(f"{cls_name}.create()")
                HBNBCommand().onecmd(f"{cls_name}.show({cls_id})")
            output = f.getvalue().strip()
            self.assertEqual(expected, output)

    def test_do_destroy_Base(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "BaseModel"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Base2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_User(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "User"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_User2(self):
        """test destroy"""
        id = ""
        cls_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Amen(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Amenity"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Amen2(self):
        """test destroy"""
        id = ""
        cls_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_City(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "City"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_City2(self):
        """test destroy"""
        id = ""
        cls_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Place(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Place"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Place2(self):
        """test destroy"""
        id = ""
        cls_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Review(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "Review"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_Review2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_State(self):
        """test destroy"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"destroy {cls_name} {id}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_State2(self):
        """test destroy"""
        id = ""
        cls_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls_name}.destroy({id})")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            self.assertEqual(len(dictionary), 0)

    def test_do_destroy_arg1_miss(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_destroy_arg1_miss2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f".destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_destroy_arg1_incorrect(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy hi")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_destroy_arg1_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"hi.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_destroy_arg2_miss(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_destroy_arg2_miss2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_destroy_arg2_incorrect(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel 123")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_destroy_arg2_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy(123)")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_all(self):
        """test all"""
        id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all")
            output = f.getvalue().strip()
            self.assertEqual(output,  "[]")
        with patch('sys.stdout', new=StringIO()) as f:
            cls_name = "State"
            HBNBCommand().onecmd(f"create {cls_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"State.{id}"]) + '"]'
            self.assertEqual(rep,  output)

    def test_do_all_Base(self):
        """test all"""
        id = ""
        cls1_name = "BaseModel"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_User(self):
        """test all"""
        id = ""
        cls1_name = "User"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Amen(self):
        """test all"""
        id = ""
        cls1_name = "Amenity"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_City(self):
        """test all"""
        id = ""
        cls1_name = "City"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Place(self):
        """test all"""
        id = ""
        cls1_name = "Place"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Review(self):
        """test all"""
        id = ""
        cls1_name = "Review"
        cls2_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_State(self):
        """test all"""
        id = ""
        cls1_name = "State"
        cls2_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls2_name}")
            output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all {cls1_name}")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls1_name}.all()")
            output = f.getvalue().strip()
            dictionary = models.storage.all()
            rep = '["' + str(dictionary[f"{cls1_name}.{id}"]) + '"]'
            self.assertEqual(rep, output)

    def test_do_all_Err(self):
        """test all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all No")
            output = f.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

    def test_do_update_Base(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mariam"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam")

    def test_do_update_Base2(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, "mar")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")

    def test_do_update_Base3(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_Base4(self):
        """test update"""
        id = ""
        cls1_name = "BaseModel"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": 'mariam ibrahim'}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_User(self):
        """test update"""
        id = ""
        cls1_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} first_name "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].first_name, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} password "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].password, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} last_name "ma"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].last_name, "ma")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} email "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].email, "mar")

    def test_do_update_User2(self):
        """test update"""
        id = ""
        cls1_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, first_name, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].first_name, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, last_name, r)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].last_name, "r")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, email, i)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].email, "i")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, password, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].password, "m")

    def test_do_update_User3(self):
        """test update"""
        id = ""
        cls1_name = "User"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"first_name": "mariam", "last_name": "nimo",
                       "email": "lol", "password": "hi"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].first_name, "mariam")
            self.assertEqual(dictionary[key].last_name, "nimo")
            self.assertEqual(dictionary[key].email, "lol")
            self.assertEqual(dictionary[key].password, "hi")

    def test_do_update_Amen(self):
        """test update"""
        id = ""
        cls1_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mam"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mam")

    def test_do_update_Amen2(self):
        """test update"""
        id = ""
        cls1_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "m")

    def test_do_update_Amen3(self):
        """test update"""
        id = ""
        cls1_name = "Amenity"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_City(self):
        """test update"""
        id = ""
        cls1_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} state_id "989"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].state_id, "989")

    def test_do_update_City2(self):
        """test update"""
        id = ""
        cls1_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, state_id "99")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].state_id, "99")

    def test_do_update_City3(self):
        """test update"""
        id = ""
        cls1_name = "City"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim", "state_id": "989"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")
            self.assertEqual(dictionary[key].state_id, "989")

    def test_do_update_Place(self):
        """test update"""
        id = ""
        cls1_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} city_id "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].city_id, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} user_id "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} description "mar"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].description, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} number_rooms "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_rooms, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} number_rooms "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_rooms, 7)
            atr = "number_bathrooms"
            HBNBCommand().onecmd(f'update {cls1_name} {id} {atr} "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_bathrooms, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "number_bathrooms"
            HBNBCommand().onecmd(f'update {cls1_name} {id} {atr} "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_bathrooms, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} max_guest "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].max_guest, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} max_guest "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].max_guest, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} price_by_night "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].price_by_night, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "price_by_night"
            HBNBCommand().onecmd(f'update {cls1_name} {id} {atr} "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].price_by_night, 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} latitude "7"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].latitude, 7.0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} longitude "7.5"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].longitude, 7.5)

    def test_do_update_Place2(self):
        """test update"""
        id = ""
        cls1_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, city_id "mar")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].city_id, "mar")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, user_id "m")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name "mariam")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, description, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].description, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "number_rooms"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_rooms, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "number_bathrooms"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].number_bathrooms, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, max_guest, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].max_guest, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "price_by_night"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].price_by_night, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "latitude"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2.3")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].latitude, 2.3)
        with patch('sys.stdout', new=StringIO()) as f:
            atr = "longitude"
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {atr}, "2.3")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].longitude, 2.3)

    def test_do_update_Place3(self):
        """test update"""
        id = ""
        cls1_name = "Place"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"city_id": "mariam ibrahim", "user_id": "nimo mohamed",
                       "name": "lol", "description": "hi"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            att_val = {"number_rooms": "9", "number_bathrooms": "2",
                       "max_guest": "3", "price_by_night": "10.6"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            att_val = {"latitude": "9.5", "longitude": "2.4"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].city_id, "mariam ibrahim")
            self.assertEqual(dictionary[key].user_id, "nimo mohamed")
            self.assertEqual(dictionary[key].name, "lol")
            self.assertEqual(dictionary[key].description, "hi")
            self.assertEqual(dictionary[key].number_rooms, 9)
            self.assertEqual(dictionary[key].number_bathrooms, 2)
            self.assertEqual(dictionary[key].max_guest, 3)
            self.assertEqual(dictionary[key].price_by_night, 10)
            self.assertEqual(dictionary[key].latitude, 9.5)
            self.assertEqual(dictionary[key].longitude, 2.4)

    def test_do_update_Review(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} place_id "mari"')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].place_id, "mari")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} user_id "989" e p')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "989")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} text "hhhh" extr')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].text, "hhhh")

    def test_do_update_Review2(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, place_id, m)')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].place_id, "m")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, user_id, "9")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].user_id, "9")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, text, "999")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].text, "999")

    def test_do_update_Review3(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            atr_val = {"place_id": "mariam ibrahim", "user_id": "989",
                       "text": "hhhh"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(atr_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].place_id, "mariam ibrahim")
            self.assertEqual(dictionary[key].user_id, "989")
            self.assertEqual(dictionary[key].text, "hhhh")

    def test_do_update_State(self):
        """test update"""
        id = ""
        cls1_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update {cls1_name} {id} name "mari" extra')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mari")

    def test_do_update_State2(self):
        """test update"""
        id = ""
        cls1_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, name, "mar")')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mar")

    def test_do_update_State3(self):
        """test update"""
        id = ""
        cls1_name = "State"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            att_val = {"name": "mariam ibrahim"}
            HBNBCommand().onecmd(f'{cls1_name}.update({id}, {str(att_val)})')
            dictionary = models.storage.all()
            key = f"{cls1_name}.{id}"
            self.assertEqual(dictionary[key].name, "mariam ibrahim")

    def test_do_update_arg1_miss(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_update_arg1_miss2(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f".update()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class name missing **")

    def test_do_update_arg1_incorrect(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update hi")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_update_arg1_incorrect2(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"hi.update()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** class doesn't exist **")

    def test_do_update_arg2_miss(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_update_arg2_miss2(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update()")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** instance id missing **")

    def test_do_update_arg2_incorrect(self):
        """test update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel 123")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_update_arg2_incorrect2(self):
        """test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(123)")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** no instance found **")

    def test_do_update_arg3_miss(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {id}")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** attribute name missing **")

    def test_do_update_arg3_miss2(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({id})")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** attribute name missing **")

    def test_do_update_arg4_miss(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {id} hi")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** value missing **")

    def test_do_update_arg4_miss2(self):
        """test update"""
        id = ""
        cls1_name = "Review"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls1_name}")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({id}, hi)")
            output = f.getvalue().strip()
            self.assertEqual(output,  "** value missing **")

    def test_invalid(self):
        """test invalid"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"crea")
            output = f.getvalue().strip()
            self.assertEqual(output,  "*** Unknown syntax: crea")

    def tearDown(self):
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
