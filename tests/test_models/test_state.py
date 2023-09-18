#!/usr/bin/python3
"""
Contains class TestState.
"""
import unittest
import os
import json
import uuid
import re
from datetime import datetime
import models
from models.state import State


class TestState(unittest.TestCase):
    """
    Tests class State.
    """
    def test_inist(self):
        """
        Testing instance: name
        """
        my_model = State()
        self.assertEqual(type(my_model), State)
        d = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.created_at.replace(microsecond=0), d)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
        self.assertEqual(my_model.name, "")
        self.assertTrue(type(my_model.id) is str)
        my_model.name = "Kenya"
        self.assertEqual(my_model.name, "Kenya")

    def test_str(self):
        """
        Testing str representation.
        """
        my_model = State()
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[State]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_str_not_empty(self):
        """
        Testing string that's not empty.
        """
        my_model = State()
        my_model.name = "Egypt"
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[State]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_save(self):
        """
        Testing updated_at.
        """
        my_model = State()
        updated = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated, my_model.updated_at)

    def test_save_not(self):
        """
        Testing updated_at.
        """
        my_model = State()
        updated = my_model.updated_at
        my_model.name = "Egypt"
        self.assertEqual(updated, my_model.updated_at)

    def test_to_dict(self):
        """
        Testing dict.
        """
        my_model = State()
        my_model_json = my_model.__dict__.copy()
        my_model_json["__class__"] = "State"
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        from_js_dict = my_model.to_dict()
        self.assertDictEqual(my_model_json, from_js_dict)

    def test_kwargs(self):
        """
        Test for kwargs.
        """
        my_model = State()
        my_model_json = my_model.__dict__.copy()
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        my_new_model = State(**my_model_json)
        self.assertTrue(type(my_new_model.id) is str)
        self.assertEqual(my_model.id, my_new_model.id)
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
