#!/usr/bin/python3
"""UWUnit tests for def max_integer(list=[]):"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """da UWUnit tests"""
    def test_empty(self):
        """what if empty list?"""
        self.assertEqual(max_integer([]), None)
    def test_jennys_phone(self):
        """what if jenny phone number?"""
        jenny = [8, 6, 7, 5, 3, 0, 9]
        self.assertEqual(max_integer(jenny), 9)
    def test_richard(self):
        dick = "richard"
        self.assertEqual(max_integer(dick), 'r')
    def test_no_richard(self):
        dick = ""
        self.assertEqual(max_integer(dick), None)

if __name__ == '__main__':
    unittest.main()
