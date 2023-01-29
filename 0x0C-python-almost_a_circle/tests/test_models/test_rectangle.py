#!/usr/bin/python3
"""unit tests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRect(unittest.TestCase):
    """da UWUnit tests"""

    def test_rekt_base(self):
        self.assertIsInstance(Rectangle(2, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_no_height(self):
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_min_args(self):
        rekt1 = Rectangle(2, 2)
        self.assertEqual(rekt1.area(), 4)

    def test_multi_rect(self):
        rekt1 = Rectangle(1, 1)
        rekt2 = Rectangle(1, 1)
        self.assertEqual(rekt1.id, rekt2.id - 1)

    def test_arg_limit(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 2, 2, 2)

    def test_privacy(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__width)

if __name__ == '__main__':
    unittest.main()
