#!/usr/bin/python3
"""
test_base
"""

import unittest
import json
from models.review import Review
from datetime import datetime
import uuid
import re
import os
import models


class test_base(unittest.TestCase):
    """class for testing the city"""

    def test_inist(self):
        """testing instances
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string"""
        my_model = Review()
        self.assertEqual(type(my_model), Review)
        d = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.created_at.replace(microsecond=0), d)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
        self.assertEqual(my_model.text, "")
        self.assertEqual(my_model.place_id, "")
        self.assertEqual(my_model.user_id, "")
        self.assertTrue(type(my_model.id) is str)
        my_model.text = "Betty"
        my_model.place_id = "hi"
        my_model.user_id = "bye"
        self.assertEqual(my_model.text, "Betty")
        self.assertEqual(my_model.place_id, "hi")
        self.assertEqual(my_model.user_id, "bye")

    def test_str(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        my_model = Review()
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Review]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_str_no_empty(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        my_model = Review()
        my_model.text = "Betty"
        my_model.place_id = "hi"
        my_model.user_id = "bye"
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Review]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_save(self):
        """check if updated at changes"""
        my_model = Review()
        updated = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated, my_model.updated_at)

    def test_save_not(self):
        """check if updated doesn't change"""
        my_model = Review()
        updated = my_model.updated_at
        my_model.text = "hi@hi"
        self.assertEqual(updated, my_model.updated_at)

    def test_to_dict(self):
        """check dict"""
        my_model = Review()
        my_model_json = my_model.__dict__.copy()
        my_model_json["__class__"] = "Review"
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        from_js_dict = my_model.to_dict()
        self.assertDictEqual(my_model_json, from_js_dict)

    def test_kwargs(self):
        """test for kwargs"""
        my_model = Review()
        my_model_json = my_model.__dict__.copy()
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        my_new_model = Review(**my_model_json)
        self.assertTrue(type(my_new_model.id) is str)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(type(my_new_model), Review)
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
