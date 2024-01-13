"""
base model test suite module
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class
    """

    def setUp(self):
        """
        Set up a new instance of BaseModel for testing
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.base_model

    def test_init_no_args(self):
        """
        Test the __init__ method without any arguments
        """
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    @patch('models.engine.storage.save')
    def test_save_method(self, mock_save):
        """
        Test the save method
        """
        self.base_model.save()
        # Ensure the storage save method is called
        mock_save.assert_called_once()
        # Ensure updated_at is updated
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str_method(self):
        """
        Test the __str__ method
        """
        str_representation = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__, str_representation)
        self.assertIn(self.base_model.id, str_representation)

    def test_init_with_args(self):
        """
        Test the __init__ method with arguments
        """
        new_base_model = BaseModel(id="123",
                                   created_at="2023-01-01T12:00:00.000000")
        self.assertEqual(new_base_model.id, "123")
        self.assertEqual(new_base_model.created_at,
                         datetime(2023, 1, 1, 12, 0, 0))


if __name__ == '__main__':
    unittest.main()
