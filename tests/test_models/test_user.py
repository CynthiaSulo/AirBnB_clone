#!/usr/bin/python3
"""
test_base
"""

import unittest
import json
from models.user import User
from datetime import datetime
import uuid
import re
import os
import models


class test_base(unittest.TestCase):
    """class for testing the usee"""

    def test_inist(self):
        """testing instances
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string"""
        my_model = User()
        self.assertEqual(type(my_model), User)
        d = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.created_at.replace(microsecond=0), d)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
        self.assertEqual(my_model.first_name, "")
        self.assertEqual(my_model.last_name, "")
        self.assertEqual(my_model.password, "")
        self.assertEqual(my_model.email, "")
        self.assertTrue(type(my_model.id) is str)
        my_model.first_name = "Betty"
        my_model.last_name = "Bar"
        my_model.email = "airbnb@mail.com"
        my_model.password = "root"
        self.assertEqual(my_model.first_name, "Betty")
        self.assertEqual(my_model.last_name, "Bar")
        self.assertEqual(my_model.email, "airbnb@mail.com")
        self.assertEqual(my_model.password, "root")

    def test_str(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        my_model = User()
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[User]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_str_no_empty(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        my_model = User()
        my_model.first_name = "Betty"
        my_model.last_name = "Bar"
        my_model.email = "airbnb@mail.com"
        my_model.password = "root"
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[User]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_save(self):
        """check if updated at changes"""
        my_model = User()
        updated = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated, my_model.updated_at)

    def test_save_not(self):
        """check if updated doesn't change"""
        my_model = User()
        updated = my_model.updated_at
        my_model.email = "hi@hi"
        self.assertEqual(updated, my_model.updated_at)

    def test_to_dict(self):
        """check dict"""
        my_model = User()
        my_model_json = my_model.__dict__.copy()
        my_model_json["__class__"] = "User"
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        from_js_dict = my_model.to_dict()
        self.assertDictEqual(my_model_json, from_js_dict)

    def test_kwargs(self):
        """test for kwargs"""
        my_model = User()
        my_model_json = my_model.__dict__.copy()
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        my_new_model = User(**my_model_json)
        self.assertTrue(type(my_new_model.id) is str)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(type(my_new_model), User)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertTrue(my_model is not my_new_model)

    def tearDown(self):
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
