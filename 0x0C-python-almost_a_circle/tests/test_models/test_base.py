#!/usr/bin/python3
# test_base.py
"""
Unit Tests for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test suite for the Base class
    """

    def test_constructor(self):
        """
        Test constructor method
        """
        # Test initialization with no arguments
        b1 = Base()
        self.assertEqual(b1.id, 1)

        # Test initialization with custom id
        b2 = Base(10)
        self.assertEqual(b2.id, 10)

        # Test initialization with multiple instances
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """
        Test to_json_string method
        """
        # Test with empty list
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        # Test with list of dictionaries
        list_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_str = Base.to_json_string(list_dicts)
        expected_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(json_str, expected_str)

    def test_from_json_string_empty_string(self):
        """
        Test from_json_string method with an empty string
        """
        json_string = "[]"
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        """
        Test from_json_string method with None
        """
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid_json(self):
        """
        Test from_json_string method with a valid JSON string
        """
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

