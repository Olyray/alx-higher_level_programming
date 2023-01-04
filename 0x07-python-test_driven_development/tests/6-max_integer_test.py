#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer function"""

    def test_empty_list(self):
        """Test the case where the input list is empty"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_one_element_list(self):
        """Test the case where the input list has a single element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_multiple_elements(self):
        """Test the case where the input list has multiple elements"""
        result = max_integer([3, 6, 1, 8, 4])
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        """Test the case where the input list has negative numbers"""
        result = max_integer([-5, -2, -9, -4])
        self.assertEqual(result, -2)

    def test_repeated_numbers(self):
        """Test the case where the input list has repeated numbers"""
        result = max_integer([3, 3, 3, 3, 3, 3])
        self.assertEqual(result, 3)

    def test_mixed_numbers(self):
        """Test the case where the input list has both positive and
        negative numbers
        """
        result = max_integer([-1, 4, -5, 7, -3])
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
