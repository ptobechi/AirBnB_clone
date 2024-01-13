"""
place unittest module
"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class
    """

    def setUp(self):
        """
        Set up a new instance of Place for testing
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.place

    def test_inheritance(self):
        """
        Test if Place inherits from BaseModel
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """
        Test if Place has the required attributes
        """
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longtitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longtitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_city_id_assignment(self):
        """
        Test if the city_id attribute can be assigned
        """
        self.place.city_id = "123"
        self.assertEqual(self.place.city_id, "123")

    def test_user_id_assignment(self):
        """
        Test if the user_id attribute can be assigned
        """
        self.place.user_id = "456"
        self.assertEqual(self.place.user_id, "456")

    # Add similar tests for other attributes

    def test_init_with_args(self):
        """
        Test the __init__ method with arguments
        """
        place_with_args = Place(id="789",
                                created_at="2023-01-01T12:00:00.000000",
                                city_id="123", user_id="456",
                                name="Cozy Place",
                                description="A beautiful cozy place",
                                number_rooms=2, number_bathrooms=1,
                                max_guest=4, price_by_night=100,
                                latitude=40.7128, longtitude=-74.0060,
                                amenity_ids=["1", "2", "3"])
        self.assertEqual(place_with_args.id, "789")
        # Add assertions for other attributes

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        obj_dict = self.place.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('city_id', obj_dict)
        self.assertIn('user_id', obj_dict)
        # Add assertions for other attributes

    def test_str_method(self):
        """
        Test the __str__ method
        """
        str_representation = str(self.place)
        self.assertIn(self.place.__class__.__name__, str_representation)
        self.assertIn(self.place.id, str_representation)


if __name__ == '__main__':
    unittest.main()
