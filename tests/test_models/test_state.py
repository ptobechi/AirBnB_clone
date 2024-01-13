"""
state module inittest
"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    Unit tests for the State class
    """

    def setUp(self):
        """
        Set up a new instance of State for testing
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.state

    def test_inheritance(self):
        """
        Test if State inherits from BaseModel
        """
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """
        Test if State has the required attributes
        """
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_name_assignment(self):
        """
        Test if the name attribute can be assigned
        """
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_init_with_args(self):
        """
        Test the __init__ method with arguments
        """
        state_with_args = State(id="789",
                                created_at="2023-01-01T12:00:00.000000",
                                name="New York")
        self.assertEqual(state_with_args.id, "789")
        # Add assertions for other attributes

    def test_to_dict_method(self):
        """
        Test the to_dict method
        """
        obj_dict = self.state.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('name', obj_dict)

    def test_str_method(self):
        """
        Test the __str__ method
        """
        str_representation = str(self.state)
        self.assertIn(self.state.__class__.__name__, str_representation)
        self.assertIn(self.state.id, str_representation)


if __name__ == '__main__':
    unittest.main()
