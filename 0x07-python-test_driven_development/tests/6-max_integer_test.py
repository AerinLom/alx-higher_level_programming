#!/usr/bin/python3
"""Unittests for max_integer([..]) function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTest(unittest.TestCase):

    def test_positive_numbers(self):
        """
        Test positive values
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """
        Test negative values
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """
        Test mixed positive and negative values
        """
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        """
        Test single element list
        """
        self.assertEqual(max_integer([5]), 5)

    def test_one_negative_number(self):
        """
        Test a list containing only one negative number
        """
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """
        Test empty list
        """
        self.assertIsNone(max_integer([]))

    def test_large_list(self):
        """
        Test a list containing a large number of elements
        """
        self.assertEqual(max_integer(list(range(1000000))), 999999)

    def test_float_numbers(self):
        """
        Test a list containing float numbers
        """
        self.assertEqual(max_integer([1.5, 2.7, 3.8]), 3.8) 

    def test_list_with_none_values(self):
        """
        Test a list containing None values
        """
        with self.assertRaises(TypeError):
            max_integer([None, None, None])

    def test_mixed_types(self):
        """
        Test a list containing a combination of different types
        """
        mixed_list = [1, 2.5, "hello", None, -5]
        with self.assertRaises(TypeError):
            max_integer(mixed_list)

if __name__ == '__main__':
    unittest.main()
