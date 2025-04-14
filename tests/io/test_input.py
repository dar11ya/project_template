import unittest
import os

from app.io.input import input_from_file_builtin, input_from_file_pandas

class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        """Create a test file before each test"""
        self.test_file = "tests/io/test_data.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("First line\nSecond line\nThird line")

    def tearDown(self):
        """Delete the file after each test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_builtin_reading(self):
        expected = "First line\nSecond line\nThird line"
        result = input_from_file_builtin(self.test_file)
        self.assertEqual(result, expected)

    def test_pandas_reading(self):
        expected = "First line\nSecond line\nThird line"
        result = input_from_file_pandas(self.test_file)
        self.assertEqual(result, expected)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_builtin("notexisting_file.txt")

if __name__ == '__main__':
    unittest.main()
