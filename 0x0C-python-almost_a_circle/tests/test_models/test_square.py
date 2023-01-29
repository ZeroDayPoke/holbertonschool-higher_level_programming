#!/usr/bin/python3
"""unit tests for square.py"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """da UWUnit tests"""
    def test_if_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_if_rekt(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_flt(self):
        with self.assertRaises(TypeError):
            Square(2.2)

    def test_non(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_chr(self):
        with self.assertRaises(TypeError):
            Square('a')

    def test_str(self):
        with self.assertRaises(TypeError):
            Square("UWU")

    def test_boo(self):
        with self.assertRaises(TypeError):
            Square(True)

    def test_lst(self):
        with self.assertRaises(TypeError):
            Square([2, 2])

    def test_dic(self):
        with self.assertRaises(TypeError):
            Square({"size": 1})

    def test_set(self):
        with self.assertRaises(TypeError):
            Square({1, 1})

    def test_tup(self):
        with self.assertRaises(TypeError):
            Square((1, 1))

    def test_ngv(self):
        with self.assertRaises(ValueError):
            Square(-3)

    def test_zed(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_update_1(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2)
        self.assertEqual(sqr1.id, 2)

    def test_update_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2)
        self.assertEqual(sqr1.size, 2)

    def test_update_3(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2, 2)
        self.assertEqual(sqr1.x, 2)

    def test_update_4(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2, 2, 2)
        self.assertEqual(sqr1.y, 2)

    def test_upd_kwa_1(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(id=2)
        self.assertEqual(sqr1.id, 2)

    def test_upd_kwa_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(size=2)
        self.assertEqual(sqr1.size, 2)

    def test_upd_kwa_3(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(x=2)
        self.assertEqual(sqr1.x, 2)

    def test_upd_kwa_4(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(y=2)
        self.assertEqual(sqr1.y, 2)

    def test_str_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        sqrstr1 = sqr1.__str__()
        sqrstr2 = '[Square] (1) 1/1 - 1'
        self.assertEqual(sqrstr1, sqrstr2)

if __name__ == '__main__':
    unittest.main()
