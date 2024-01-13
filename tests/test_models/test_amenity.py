import unittest
from models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class
    """

    def setUp(self):
        """
        Set up a new instance of Amenity for testing
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.amenity

    def test_inheritance(self):
        """
        Test if Amenity inherits from BaseModel
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """
        Test if Amenity has the required attributes
        """
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        """
        Test if the name attribute can be assigned
        """
        self.amenity.name = "WiFi"
        self.assertEqual(self.amenity.name, "WiFi")

    def test_init_with_args(self):
        """
        Test the __init__ method with arguments
        """
        amenity_with_args = Amenity(id="123",
                                    created_at="2023-01-01T12:00:00.000000",
                                    name="WiFi")
        self.assertEqual(amenity_with_args.id, "123")
        self.assertEqual(amenity_with_args.created_at,
                         datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(amenity_with_args.name, "WiFi")

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        obj_dict = self.amenity.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('name', obj_dict)

    def test_str_method(self):
        """
        Test the __str__ method
        """
        str_representation = str(self.amenity)
        self.assertIn(self.amenity.__class__.__name__, str_representation)
        self.assertIn(self.amenity.id, str_representation)

if __name__ == '__main__':
    unittest.main()
