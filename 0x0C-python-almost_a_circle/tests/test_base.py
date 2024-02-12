#!/usr/bin/python3

# test_base.py
"""
Unit Tests for Base class
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test suite for the Base class
    """

    def test_constructor(self):
        """
        Test base constructor method
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


class TestToJsonString(unittest.TestCase):
    """
    Unittests for the to_json_string method
    """

    def test_to_json_string(self):
        # Test with empty list
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        # Test with list of dictionaries
        list_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_str = Base.to_json_string(list_dicts)
        expected_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(json_str, expected_str)


class TestFromJsonString(unittest.TestCase):
    """
    Unittests for the from_json_string method
    """

    def test_from_json_string_empty_string(self):
        json_string = "[]"
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid_json(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        self.assertEqual(result, expected)


class TestCreate(unittest.TestCase):
    """
    Unittests for the create method
    """

    def test_create_original_square_instance(self):
        square_original = Square(5, 7, 2, 9)
        square_original_dict = square_original.to_dictionary()
        square_created = Square.create(**square_original_dict)
        self.assertEqual("[Square] (9) 7/2 - 5", str(square_original))

    def test_create_new_rectangle_instance(self):
        rectangle_new = Rectangle(4, 6, 2, 3, 9)
        rectangle_new_dict = rectangle_new.to_dictionary()
        rectangle_created = Rectangle.create(**rectangle_new_dict)
        self.assertEqual("[Rectangle] (9) 2/3 - 4/6", str(rectangle_created))

    def test_square_instance_equality(self):
        square1 = Square(5, 7, 2, 9)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertNotEqual(square1, square2)

    def test_create_original_rectangle_instance(self):
        rectangle_original = Rectangle(4, 6, 2, 3, 9)
        rectangle_original_dict = rectangle_original.to_dictionary()
        rectangle_created = Rectangle.create(**rectangle_original_dict)
        self.assertEqual("[Rectangle] (9) 2/3 - 4/6", str(rectangle_original))

    def test_rectangle_instance_identity(self):
        rectangle1 = Rectangle(4, 6, 2, 3, 9)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertIsNot(rectangle1, rectangle2)

    def test_create_new_square_instance(self):
        square_new = Square(5, 7, 2, 9)
        square_new_dict = square_new.to_dictionary()
        square_created = Square.create(**square_new_dict)
        self.assertEqual("[Square] (9) 7/2 - 5", str(square_created))

    def test_rectangle_instance_inequality(self):
        rectangle1 = Rectangle(4, 6, 2, 3, 9)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_square_instance_identity(self):
        square1 = Square(5, 7, 2, 9)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertIsNot(square1, square2)


class TestBase_load_from_file(unittest.TestCase):
    """
    Unittests for testing load_from_file_method
    """

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_first_rectangle_instance_loaded_from_file(self):
        rect_first = Rectangle(5, 10, 3, 2, 11)
        rect_second = Rectangle(7, 3, 2, 1, 12)
        Rectangle.save_to_file([rect_first, rect_second])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(str(rect_first), str(rectangles[0]))

    def test_second_rectangle_instance_loaded_from_file(self):
        rect_first = Rectangle(5, 10, 3, 2, 11)
        rect_second = Rectangle(7, 3, 2, 1, 12)
        Rectangle.save_to_file([rect_first, rect_second])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(str(rect_second), str(rectangles[1]))

    def test_first_square_instance_loaded_from_file(self):
        square_first = Square(6, 4, 2, 13)
        square_second = Square(8, 3, 5, 14)
        Square.save_to_file([square_first, square_second])
        squares = Square.load_from_file()
        self.assertEqual(str(square_first), str(squares[0]))

    def test_second_square_instance_loaded_from_file(self):
        square_first = Square(6, 4, 2, 13)
        square_second = Square(8, 3, 5, 14)
        Square.save_to_file([square_first, square_second])
        squares = Square.load_from_file()
        self.assertEqual(str(square_second), str(squares[1]))

    def test_rectangle_types_loaded_from_file(self):
        rect_first = Rectangle(5, 10, 3, 2, 11)
        rect_second = Rectangle(7, 3, 2, 1, 12)
        Rectangle.save_to_file([rect_first, rect_second])
        rectangles = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in rectangles))

    def test_square_types_loaded_from_file(self):
        square_first = Square(6, 4, 2, 13)
        square_second = Square(8, 3, 5, 14)
        Square.save_to_file([square_first, square_second])
        squares = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in squares))

    def test_multiple_args_loaded_from_file(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == '__main__':
    unittest.main()
