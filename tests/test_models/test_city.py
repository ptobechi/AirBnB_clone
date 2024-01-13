"""
a test module
"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class
    """

    def setUp(self):
        """
        Set up a new instance of City for testing
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.city

    def test_inheritance(self):
        """
        Test if City inherits from BaseModel
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """
        Test if City has the required attributes
        """
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_name_assignment(self):
        """
        Test if the name attribute can be assigned
        """
        self.city.name = "New York"
        self.assertEqual(self.city.name, "New York")

    def test_state_id_assignment(self):
        """
        Test if the state_id attribute can be assigned
        """
        self.city.state_id = "NY"
        self.assertEqual(self.city.state_id, "NY")

    def test_init_with_args(self):
        """
        Test the __init__ method with arguments
        """
        city_with_args = City(id="123",
                              created_at="2023-01-01T12:00:00.000000",
                              name="New York", state_id="NY")
        self.assertEqual(city_with_args.id, "123")
        self.assertEqual(city_with_args.created_at,
                         datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(city_with_args.name, "New York")
        self.assertEqual(city_with_args.state_id, "NY")

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        obj_dict = self.city.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('state_id', obj_dict)

    def test_str_method(self):
        """
        Test the __str__ method
        """
        str_representation = str(self.city)
        self.assertIn(self.city.__class__.__name__, str_representation)
        self.assertIn(self.city.id, str_representation)


if __name__ == '__main__':
    unittest.main()
