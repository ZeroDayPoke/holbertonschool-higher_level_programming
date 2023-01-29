#!/usr/bin/python3
"""unit tests for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """da UWUnit tests"""
    def test_no_arg(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

if __name__ == '__main__':
    unittest.main()
