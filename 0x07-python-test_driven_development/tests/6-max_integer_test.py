#!/usr/bin/python3
"""UWUnit tests for def max_integer(list=[]):"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """da UWUnit tests"""
    def test_empty(self):
        """what if empty list?"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
