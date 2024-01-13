"""
user module test suite
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class
    """

    def setUp(self):
        """
        Set up a new instance of User for testing
        """
        self.user = User()

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.user

    def test_inheritance(self):
        """
        Test if User inherits from BaseModel
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """
        Test if User has the required attributes
        """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        """
        Test if attributes can be assigned
        """
        self.user.email = "user@example.com"
        self.user.password = "securepassword"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_init_with_args(self):
        """
        Test the __init__ method with arguments
        """
        user_with_args = User(id="123",
                              created_at="2023-01-01T12:00:00.000000",
                              email="user@example.com",
                              password="securepassword",
                              first_name="John", last_name="Doe")
        self.assertEqual(user_with_args.id, "123")
        # Add assertions for other attributes

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        obj_dict = self.user.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('email', obj_dict)
        self.assertIn('password', obj_dict)
        self.assertIn('first_name', obj_dict)
        self.assertIn('last_name', obj_dict)

    def test_str_method(self):
        """
        Test the __str__ method
        """
        str_representation = str(self.user)
        self.assertIn(self.user.__class__.__name__, str_representation)
        self.assertIn(self.user.id, str_representation)


if __name__ == '__main__':
    unittest.main()
