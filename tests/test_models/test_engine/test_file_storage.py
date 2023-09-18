#!/usr/bin/python3
"""
file storage tests
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City
import models
import unittest
import json
import os


class TestFileStorage(unittest.TestCase):
    """
    testing file storage
    """

    def setUp(self):
        """allocating resources"""
        models.storage._FileStorage__objects = {}

    def test_attr(self):
        """testing initialization"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_attr_str(self):
        """testing initialization"""
        self.assertEqual(type(models.storage._FileStorage__file_path), str)

    def test_attr_str_ex(self):
        """testing initialization"""
        self.assertEqual(models.storage._FileStorage__file_path, "file.json")

    def test_attr_inst(self):
        """testing initialization"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_attr_str_cls(self):
        """testing initialization"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_attr_str_ex_cls(self):
        """testing initialization"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_attr_dict_cls(self):
        """testing initialization"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_attr_empty_dict_cls(self):
        """testing initialization"""
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_attr_dict_ex(self):
        """testing initialization"""
        obj_dict = models.storage._FileStorage__objects
        expected_dict = {}
        self.assertEqual(models.storage._FileStorage__objects, expected_dict)

    def test_attr_dict(self):
        """testing initialization"""
        self.assertEqual(type(models.storage._FileStorage__objects), dict)

    def test_attr_empty_dict(self):
        """testing initialization"""
        self.assertEqual(models.storage._FileStorage__objects, {})

    def test_inst_arg(self):
        """error when calling"""
        with self.assertRaises(TypeError):
            FileStorage("arg")

    def test_all_arg(self):
        """error when calling"""
        with self.assertRaises(TypeError):
            models.storage.all("arg")

    def test_new_arg(self):
        """error when calling"""
        my_model = BaseModel()
        with self.assertRaises(TypeError):
            models.storage.new(my_model, "arg")

    def test_new_no_arg(self):
        """error when calling"""
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_new_none(self):
        """error when calling"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_arg(self):
        """error when calling"""
        with self.assertRaises(TypeError):
            models.storage.save("arg")

    def test_reload_arg(self):
        """error when calling"""
        with self.assertRaises(TypeError):
            models.storage.reload("arg")

    def test_all(self):
        """testing all"""
        all_objs = models.storage.all()
        self.assertEqual(type(all_objs), dict)
        self.assertEqual(len(all_objs), 0)

    def test_new_not(self):
        """testing new"""
        my_model = BaseModel()
        my_model_json = my_model.__dict__.copy()
        my_model_json["created_at"] = my_model.created_at.isoformat()
        my_model_json["updated_at"] = my_model.updated_at.isoformat()
        my_new_model = BaseModel(**my_model_json)
        all_objs = models.storage.all()
        key = my_model.__class__.__name__ + '.' + my_model.id
        self.assertEqual(all_objs[key], my_model)
        self.assertEqual(len(all_objs), 1)

    def test_new_BaseModel(self):
        """testing new"""
        obj = BaseModel()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(all_objs[key], obj)

    def test_new_User(self):
        """testing new"""
        obj = User()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(all_objs[key], obj)

    def test_new_Amenity(self):
        """testing new"""
        obj = Amenity()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(all_objs[key], obj)

    def test_new_City(self):
        """testing new"""
        obj = City()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(all_objs[key], obj)

    def test_new_Place(self):
        """testing new"""
        obj = Place()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(all_objs[key], obj)

    def test_new_Review(self):
        """testing new"""
        obj = Review()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(all_objs[key], obj)

    def test_new_State(self):
        """testing new"""
        obj = State()
        models.storage.new(obj)
        all_objs = models.storage.all()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(all_objs[key], obj)

    def test_new_all(self):
        """testing new"""
        obj = User()
        obj2 = BaseModel()
        obj3 = Amenity()
        obj4 = City()
        obj5 = Place()
        obj6 = Review()
        obj7 = State()
        list_objs = [obj, obj2, obj3, obj4, obj5, obj6, obj7]
        all_objs = models.storage.all()
        for ob in list_objs:
            key = ob.__class__.__name__ + '.' + ob.id
            self.assertEqual(all_objs[key], ob)

    def test_save_BaseModel1(self):
        """ testing save"""
        obj1 = BaseModel()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_BaseModel2(self):
        """ testing save"""
        obj1 = BaseModel()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_BaseModel(self):
        """ testing save"""
        obj1 = BaseModel()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj2 = BaseModel()
        models.storage.save()
        key2 = obj2.__class__.__name__ + '.' + obj2.id
        expected = {key: obj1.to_dict(),
                    key2: obj2.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj3 = BaseModel()
        models.storage.save()
        key3 = obj3.__class__.__name__ + '.' + obj3.id
        expected = {key: obj1.to_dict(),
                    key2: obj2.to_dict(),
                    key3: obj3.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        self.assertEqual(len(models.storage._FileStorage__objects), 3)

    def test_save_User1(self):
        """ testing save"""
        obj1 = User()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_User2(self):
        """ testing save"""
        obj1 = User()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_User(self):
        """ testing save"""
        obj1 = User()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj2 = User()
        models.storage.save()
        key2 = obj2.__class__.__name__ + '.' + obj2.id
        expected = {key: obj1.to_dict(),
                    key2: obj2.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj3 = User()
        models.storage.save()
        key3 = obj3.__class__.__name__ + '.' + obj3.id
        expected = {key: obj1.to_dict(),
                    key2: obj2.to_dict(),
                    key3: obj3.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        self.assertEqual(len(models.storage._FileStorage__objects), 3)

    def test_save_Amenity1(self):
        """ testing save"""
        obj1 = Amenity()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_Amenity(self):
        """ testing save"""
        obj1 = Amenity()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)

    def test_save_City1(self):
        """ testing save"""
        obj1 = City()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_City(self):
        """ testing save"""
        obj1 = City()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)

    def test_save_Place1(self):
        """ testing save"""
        obj1 = Place()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_Place(self):
        """ testing save"""
        obj1 = Place()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)

    def test_save_Review1(self):
        """ testing save"""
        obj1 = Review()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_Review(self):
        """ testing save"""
        obj1 = Review()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)

    def test_save_State1(self):
        """ testing save"""
        obj1 = State()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        old_updated = obj1.updated_at
        obj1.email = "hi@hi"
        obj1.save()
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertIn(key, json_file)
        self.assertFalse(old_updated == json_file[key]["updated_at"])

    def test_save_State(self):
        """ testing save"""
        obj1 = State()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)

    def test_save_all(self):
        """ testing save"""
        obj1 = User()
        models.storage.save()
        key = obj1.__class__.__name__ + '.' + obj1.id
        expected = {key: obj1.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj2 = BaseModel()
        models.storage.save()
        key2 = obj2.__class__.__name__ + '.' + obj2.id
        expected = {key: obj1.to_dict(),
                    key2: obj2.to_dict()}
        json_filename = "file.json"
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)
        obj4 = City()
        obj5 = Place()
        obj6 = Review()
        obj7 = State()
        models.storage.save()
        list_objs = [obj4, obj5, obj6, obj7]
        for ob in list_objs:
            key = ob.__class__.__name__ + '.' + ob.id
            expected[key] = ob.to_dict()
        with open(json_filename, 'r') as f:
            json_file = json.load(f)
        self.assertEqual(json_file, expected)

    def test_reload_empty(self):
        """reload no json file"""
        models.storage.reload()

    def test_reload_BaseModel(self):
        """testing reload"""
        BaseModel()
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        for key, value in obj.items():
            value.to_dict()
            value_dict.append(value.to_dict())
        value1_dict = []
        for key, value in obj1.items():
            value.to_dict()
            value1_dict.append(value.to_dict())
        self.assertEqual(value_dict, value1_dict)

    def test_reload_User(self):
        """testing reload"""
        User()
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        for key, value in obj.items():
            value.to_dict()
            value_dict.append(value.to_dict())
        value1_dict = []
        for key, value in obj1.items():
            value.to_dict()
            value1_dict.append(value.to_dict())
        self.assertEqual(value_dict, value1_dict)

    def test_reload_Amenity(self):
        """testing reload"""
        amenity = Amenity()
        key_amenity = amenity.__class__.__name__ + '.' + amenity.id
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        value_dict.append(obj[key_amenity].to_dict())
        value1_dict = []
        value1_dict.append(obj1[key_amenity].to_dict())
        self.assertEqual(value_dict, value1_dict)

    def test_reload_City(self):
        """testing reload"""
        city = City()
        key_city = city.__class__.__name__ + '.' + city.id
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        value_dict.append(obj[key_city].to_dict())
        value1_dict = []
        value1_dict.append(obj1[key_city].to_dict())
        self.assertEqual(value_dict, value1_dict)

    def test_reload_Place(self):
        """testing reload"""
        place = Place()
        key_place = place.__class__.__name__ + '.' + place.id
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        value_dict.append(obj[key_place].to_dict())
        value1_dict = []
        value1_dict.append(obj1[key_place].to_dict())
        self.assertEqual(value_dict, value1_dict)

    def test_reload_Review(self):
        """testing reload"""
        review = Review()
        key_review = review.__class__.__name__ + '.' + review.id
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        value_dict.append(obj[key_review].to_dict())
        value1_dict = []
        value1_dict.append(obj1[key_review].to_dict())
        self.assertEqual(value_dict, value1_dict)

    def test_reload_State(self):
        """testing reload"""
        state = State()
        key_state = state.__class__.__name__ + '.' + state.id
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        value_dict.append(obj[key_state].to_dict())
        value1_dict = []
        value1_dict.append(obj1[key_state].to_dict())
        self.assertEqual(value_dict, value1_dict)

    def test_reload_All(self):
        """testing reload"""
        user = User()
        base = BaseModel()
        obj3 = Amenity()
        obj4 = City()
        obj5 = Place()
        obj6 = Review()
        obj7 = State()
        key_base = base.__class__.__name__ + '.' + base.id
        key_user = user.__class__.__name__ + '.' + user.id
        key_amenity = obj3.__class__.__name__ + '.' + obj3.id
        key_city = obj4.__class__.__name__ + '.' + obj4.id
        key_place = obj5.__class__.__name__ + '.' + obj5.id
        key_review = obj6.__class__.__name__ + '.' + obj6.id
        key_state = obj7.__class__.__name__ + '.' + obj7.id
        obj = models.storage.all().copy()
        models.storage.save()
        models.storage.reload()
        obj1 = models.storage.all()
        json_filename = "file.json"
        value_dict = []
        key_list = [key_place, key_amenity, key_city, key_review, key_user,
                    key_base, key_state]
        for key in key_list:
            value_dict.append(obj[key].to_dict())
        value1_dict = []
        for key in key_list:
            value1_dict.append(obj1[key].to_dict())
        self.assertEqual(value_dict, value1_dict)

    def tearDown(self):
        """deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
