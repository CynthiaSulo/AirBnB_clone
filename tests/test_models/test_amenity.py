#!/usr/bin/python3
"""
test_base
"""

import unittest
import json
from models.amenity import Amenity
from datetime import datetime
import uuid
import re
import os
import models


class test_base(unittest.TestCase):
    """class for testing the amenity"""

    def test_inist(self):
        """testing instances
        Public class attributes:
        name: string - empty string"""
        my_model = Amenity()
        self.assertEqual(type(my_model), Amenity)
        d = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.created_at.replace(microsecond=0), d)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
        self.assertEqual(my_model.name, "")
        self.assertTrue(type(my_model.id) is str)
        my_model.name = "Betty"
        self.assertEqual(my_model.name, "Betty")

    def test_str(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        my_model = Amenity()
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Amenity]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_str_no_empty(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        my_model = Amenity()
        my_model.name = "Betty"
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Amenity]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_save(self):
        """check if updated at changes"""
        my_model = Amenity()
        updated = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated, my_model.updated_at)

    def test_save_not(self):
        """check if updated doesn't change"""
        my_model = Amenity()
        updated = my_model.updated_at
        my_model.name = "hi@hi"
        self.assertEqual(updated, my_model.updated_at)

    def test_to_dict(self):
        """check dict"""
        my_model = Amenity()
        my_model_json = my_model.__dict__.copy()
        my_model_json["__class__"] = "Amenity"
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        from_js_dict = my_model.to_dict()
        self.assertDictEqual(my_model_json, from_js_dict)

    def test_kwargs(self):
        """test for kwargs"""
        my_model = Amenity()
        my_model_json = my_model.__dict__.copy()
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        my_new_model = Amenity(**my_model_json)
        self.assertTrue(type(my_new_model.id) is str)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(type(my_new_model), Amenity)
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
