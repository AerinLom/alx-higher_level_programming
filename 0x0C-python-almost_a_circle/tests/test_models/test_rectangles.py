#!/usr/bin/python3
# test_rectangles.py
"""
Unit Tests for rectangle.py
"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Test suite for the Rectangle class
    """

    def test_constructor(self):
        """
        Test constructor method
        """
        # Test initialization with positive values
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        # Test initialization with custom position and ID
        r2 = Rectangle(15, 25, 5, 8, 300)
        self.assertEqual(r2.width, 15)
        self.assertEqual(r2.height, 25)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 8)
        self.assertEqual(r2.id, 300)

    def test_attribute_validations(self):
        """
        Test attribute validations
        """
        # Test width and height validations
        with self.assertRaises(ValueError):
            r = Rectangle(0, 25)
        with self.assertRaises(ValueError):
            r = Rectangle(30, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20)
        with self.assertRaises(ValueError):
            r = Rectangle(20, -30)
        with self.assertRaises(TypeError):
            r = Rectangle("20", 10)
        with self.assertRaises(TypeError):
            r = Rectangle(20, "10")

        # Test x and y validations
        with self.assertRaises(ValueError):
            r = Rectangle(20, 30, -5, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(20, 30, 5, -10)
        with self.assertRaises(TypeError):
            r = Rectangle(20, 30, "5", 10)
        with self.assertRaises(TypeError):
            r = Rectangle(20, 30, 5, "10")

    def test_area(self):
        """
        Test area method
        """
        r = Rectangle(8, 6)
        self.assertEqual(r.area(), 48)

        r2 = Rectangle(10, 10)
        self.assertEqual(r2.area(), 100)

    def test_display(self):
        """
        Test display method
        """
        # Redirect stdout to capture printed output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        r = Rectangle(4, 3)
        r.display()
        sys.stdout = sys.__stdout__

        # Check if the printed output matches the expected pattern
        expected_output = "####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Test display method with larger rectangle
        captured_output = StringIO()
        sys.stdout = captured_output

        r2 = Rectangle(5, 5)
        r2.display()
        sys.stdout = sys.__stdout__

        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_string_representation(self):
        """
        Test string representation method
        """
        r = Rectangle(6, 9, 2, 3, 300)
        expected_output = "[Rectangle] (300) 2/3 - 6/9"
        actual_output = str(r)
        self.assertEqual(actual_output, expected_output)

        r2 = Rectangle(8, 12, 1, 1, 56)
        expected_output2 = "[Rectangle] (56) 1/1 - 8/12"
        actual_output2 = str(r2)
        self.assertEqual(actual_output2, expected_output2)


    def test_multiple_display(self):
        """
        Test display method with multiple rectangles
        """
        # Redirect stdout to capture printed output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(2, 2)
        r2 = Rectangle(3, 3, 1, 1)
        r1.display()
        print("\n")
        r2.display()
        sys.stdout = sys.__stdout__

        # Check if the printed output matches the expected pattern
        expected_output = "##\n##\n\n\n\n ###\n ###\n ###\n"
        actual_output = captured_output.getvalue()
        print("Expected Output:\n", expected_output)
        print("Actual Output:\n", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_update(self):
        """
        Test update method
        """
        r = Rectangle(3, 4)
        r.update(5)
        self.assertEqual(r.id, 5)
        r.update(5, 6)
        self.assertEqual(r.width, 6)
        r.update(5, 6, 7)
        self.assertEqual(r.height, 7)
        r.update(5, 6, 7, 8)
        self.assertEqual(r.x, 8)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.y, 9)

        # Test update method with different values
        r.update(6, 7, 8, 9, 10)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

if __name__ == '__main__':
    unittest.main()
