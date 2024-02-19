#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(my_list), 5)

    def test_unordered_list(self):
        """Test an unordered list of integers
        """
        my_list = [3, 1, 5, 2, 4]
        self.assertEqual(max_integer(my_list), 5)

    def test_max_at_beginning(self):
        """Test when the max int is at the beginning
        of the list
        """
        my_list = [5, 2, 4, 1, 3]
        self.assertEqual(max_integer(my_list), 5)

    def test_empty_list(self):
        """Test when the list is empty
        """
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_one_element(self):
        """Test when list has just 1 element
        """
        my_list = [5]
        self.assertEqual(max_integer(my_list), 5)

    def test_floats(self):
        """Test when floats are passed in list
        """
        my_list = [3.5, 4.30, 8.25, 10.1]
        self.assertEqual(max_integer(my_list), 10.1)

    def test_int_and_float(self):
        """Test when int and floats are passed in list
        """
        my_list = [3.5, 4, 8.25, 10]
        self.assertEqual(max_integer(my_list), 10)

    def test_string(self):
        """Test when string is passed in list
        """
        my_list = "hello world"
        self.assertEqual(max_integer(my_list), 'w')

    def test_list_of_string(self):
        """Test when a list of strings is passed
        """
        my_list = ["hello", "my", "name", "is", "bob"]
        self.assertEqual(max_integer(my_list), "name")

    def test_empty_string(self):
        """Test when an empty string is passed
        """
        my_list = ""
        self.assertEqual(max_integer(my_list), None)


if __name__ == '__main__':
    unittest.main()
