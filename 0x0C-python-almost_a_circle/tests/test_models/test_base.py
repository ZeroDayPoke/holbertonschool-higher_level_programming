#!/usr/bin/python3
"""unit tests for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """da UWUnit tests"""
    def test_non(self):
        base1 = Base(None)
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_int(self):
        self.assertEqual(Base(1).id, 1)

    def test_flt(self):
        self.assertEqual(Base(1.1).id, 1.1)

    def test_chr(self):
        self.assertEqual(Base('a').id, 'a')

    def test_str(self):
        self.assertEqual(Base("hi").id, "hi")

    def test_boo(self):
        self.assertEqual(Base(True).id, True)

    def test_lst(self):
        self.assertEqual(Base([1, 1]).id, [1, 1])

    def test_dic(self):
        self.assertEqual(Base({"richard": 1}).id, {"richard": 1})

    def test_tup(self):
        self.assertEqual(Base((1, 1)).id, (1, 1))

    def test_set(self):
        self.assertEqual(Base({1, 1}).id, {1, 1})

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
