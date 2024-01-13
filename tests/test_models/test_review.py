"""
review module unittest
"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Unit tests for the Review class
    """

    def setUp(self):
        """
        Set up a new instance of Review for testing
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.review

    def test_inheritance(self):
        """
        Test if Review inherits from BaseModel
        """
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """
        Test if Review has the required attributes
        """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_assignment(self):
        """
        Test if attributes can be assigned
        """
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Nice place!"
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Nice place!")

    def test_init_with_args(self):
        """
        Test the __init__ method with arguments
        """
        review_with_args = Review(id="789",
                                  created_at="2023-01-01T12:00:00.000000",
                                  place_id="456", user_id="789",
                                  text="Great experience")
        self.assertEqual(review_with_args.id, "789")
        # Add assertions for other attributes

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        obj_dict = self.review.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('place_id', obj_dict)
        self.assertIn('user_id', obj_dict)
        self.assertIn('text', obj_dict)

    def test_str_method(self):
        """
        Test the __str__ method
        """
        str_representation = str(self.review)
        self.assertIn(self.review.__class__.__name__, str_representation)
        self.assertIn(self.review.id, str_representation)


if __name__ == '__main__':
    unittest.main()
