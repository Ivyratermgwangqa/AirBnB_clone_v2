#!/usr/bin/python3
"""Test for BaseModel"""

import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    def tearDown(self):
        """Tear down after each test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_base_model(self):
        """Check PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstrings_base_model(self):
        """Check for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_methods_exist(self):
        """Check if BaseModel has required methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_base_model(self):
        """Test if the instance is of type BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    @unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] == 'db',
                     'BaseModel not mapped')
    def test_save_base_model(self):
        """Test if the save method works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_base_model(self):
        """Test if the to_dict method produces a valid dictionary"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
