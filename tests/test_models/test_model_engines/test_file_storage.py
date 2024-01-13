import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class
    """

    def setUp(self):
        """
        Set up a new instance of FileStorage for testing
        """
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.file_storage
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """
        Test the all method
        """
        # Create some instances
        obj1 = BaseModel()
        obj2 = BaseModel()

        # Add instances to FileStorage
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        # Test all method without class filter
        all_objects = self.file_storage.all()
        self.assertIn("BaseModel.{}".format(obj1.id), all_objects)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objects)

        # Test all method with class filter
        all_base_models = self.file_storage.all(cls="BaseModel")
        self.assertIn("BaseModel.{}".format(obj1.id), all_base_models)
        self.assertIn("BaseModel.{}".format(obj2.id), all_base_models)

        # Test all method with non-existent class filter
        all_invalid_class = self.file_storage.all(cls="InvalidClass")
        self.assertEqual(len(all_invalid_class), 0)

    def test_new_method(self):
        """
        Test the new method
        """
        obj = BaseModel()
        self.file_storage.new(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.file_storage._FileStorage__objects)
        self.assertIs(self.file_storage._FileStorage__objects[key], obj)

    def test_save_method(self):
        """
        Test the save method
        """
        # Create some instances
        obj1 = BaseModel()
        obj2 = BaseModel()

        # Add instances to FileStorage
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        # Save the file
        self.file_storage.save()

        # Load the file and check if objects are present
        loaded_file_storage = FileStorage()
        loaded_file_storage._FileStorage__file_path = self.file_path
        loaded_file_storage.reload()

        key1 = "BaseModel.{}".format(obj1.id)
        key2 = "BaseModel.{}".format(obj2.id)

        self.assertIn(key1, loaded_file_storage._FileStorage__objects)
        self.assertIn(key2, loaded_file_storage._FileStorage__objects)

    def test_reload_method(self):
        """
        Test the reload method
        """
        # Create some instances
        obj1 = BaseModel()
        obj2 = BaseModel()

        # Add instances to FileStorage
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        # Save the file
        self.file_storage.save()

        # Create a new FileStorage instance and reload from the file
        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = self.file_path
        new_file_storage.reload()

        key1 = "BaseModel.{}".format(obj1.id)
        key2 = "BaseModel.{}".format(obj2.id)

        self.assertIn(key1, new_file_storage._FileStorage__objects)
        self.assertIn(key2, new_file_storage._FileStorage__objects)

    def test_reload_nonexistent_file(self):
        """
        Test reload method with a nonexistent file
        """
        # Attempt to reload from a nonexistent file
        self.file_storage._FileStorage__file_path = "nonexistent_file.json"
        self.file_storage.reload()

        # Check that __objects is still an empty dictionary
        self.assertEqual(self.file_storage._FileStorage__objects, {})

if __name__ == '__main__':
    unittest.main()
