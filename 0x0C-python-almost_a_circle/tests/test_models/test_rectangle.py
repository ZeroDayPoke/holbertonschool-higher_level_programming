#!/usr/bin/python3
"""unit tests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRect(unittest.TestCase):
    """da UWUnit tests"""
    def test_rekt_base(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

if __name__ == '__main__':
    unittest.main()
