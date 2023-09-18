#!/usr/bin/python3
"""
Contains class TestPlace.
"""
import unittest
import os
import json
import uuid
import re
from datetime import datetime
import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Tests class Place.
    """
    def test_inist(self):
        """
        Testing instances: city_id, user_id, name, description,
        number_rooms, number_bathrooms, max_guest, price_by_night,
        latitude, longitude, amenity_ids.
        """
        my_model = Place()
        self.assertEqual(type(my_model), Place)
        d = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.created_at.replace(microsecond=0), d)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
        self.assertEqual(my_model.city_id, "")
        self.assertEqual(my_model.user_id, "")
        self.assertEqual(my_model.name, "")
        self.assertEqual(my_model.description, "")
        self.assertEqual(my_model.number_rooms, 0)
        self.assertEqual(my_model.number_bathrooms, 0)
        self.assertEqual(my_model.max_guest, 0)
        self.assertEqual(my_model.price_by_night, 0)
        self.assertEqual(my_model.latitude, 0.0)
        self.assertEqual(my_model.longitude, 0.0)
        self.assertEqual(my_model.amenity_ids, [])
        self.assertTrue(type(my_model.id) is str)
        my_model.city_id = "City_id"
        my_model.user_id = "User_id"
        my_model.name = "Westlands"
        my_model.description = "Modern"
        my_model.number_rooms = 2
        my_model.number_bathrooms = 2
        my_model.max_guest = 2
        my_model.price_by_night = 100
        my_model.latitude = 3.4
        my_model.longitude = 4.5
        my_model.amenity_ids = "Amenity_id"
        self.assertEqual(my_model.city_id, "City_id")
        self.assertEqual(my_model.user_id, "User_id")
        self.assertEqual(my_model.name, "Westlands")
        self.assertEqual(my_model.description, "Modern")
        self.assertEqual(my_model.number_rooms, 2)
        self.assertEqual(my_model.number_bathrooms, 2)
        self.assertEqual(my_model.max_guest, 2)
        self.assertEqual(my_model.price_by_night, 100)
        self.assertEqual(my_model.latitude, 3.4)
        self.assertEqual(my_model.longitude, 4.5)
        self.assertEqual(my_model.amenity_ids, "Amenity_id")

    def test_str(self):
        """
        Testing str representation.
        """
        my_model = Place()
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Place]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_str_not_empty(self):
        """
        Testing string that's not empty.
        """
        my_model = Place()
        my_model.name = "Westlands"
        rep = str(my_model)
        class_name = re.search("\\[.*\\]", rep).group(0)
        self_id = re.search("\\(.{36}\\)", rep).group(0)
        self_dict = re.search("\\{.*\\}", rep).group(0)
        self.assertEqual(class_name, "[Place]")
        self.assertTrue(len(self_id) == 38)
        inst_dict = my_model.__dict__
        self.assertEqual(str(inst_dict), self_dict)

    def test_save(self):
        """
        Testing updated_at.
        """
        my_model = Place()
        updated = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated, my_model.updated_at)

    def test_save_not(self):
        """
        Testing updated_at.
        """
        my_model = Place()
        updated = my_model.updated_at
        my_model.name = "Westlands"
        self.assertEqual(updated, my_model.updated_at)

    def test_to_dict(self):
        """
        Testing dict.
        """
        my_model = Place()
        my_model_json = my_model.__dict__.copy()
        my_model_json["__class__"] = "Place"
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        from_js_dict = my_model.to_dict()
        self.assertDictEqual(my_model_json, from_js_dict)

    def test_kwargs(self):
        """
        Test for kwargs.
        """
        my_model = Place()
        my_model_json = my_model.__dict__.copy()
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        my_new_model = Place(**my_model_json)
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
