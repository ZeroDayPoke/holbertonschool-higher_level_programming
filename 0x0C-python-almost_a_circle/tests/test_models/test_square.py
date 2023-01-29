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

    def test_upd_kwa_5(self):
        sqr1 = Square(2, 2, 2, 2)
        sqr1.update(id=5, y=3)
        self.assertEqual(sqr1.id, 5)
        self.assertEqual(sqr1.y, 3)

    def test_str_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        sqrstr1 = sqr1.__str__()
        sqrstr2 = '[Square] (1) 1/1 - 1'
        self.assertEqual(sqrstr1, sqrstr2)

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__id)

    def test_privacy_2(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__size)

    def test_privacy_3(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__x)

    def test_privacy_4(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__y)

    def test_arg_limit(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_okay_sqr(self):
        sqr1 = Square(3, 0, 0, 1)
        self.assertEqual(sqr1.area(), 9)

    def test_size_init(self):
        sqr1 = Square(3)
        self.assertEqual(sqr1.width, sqr1.size)
        self.assertEqual(sqr1.height, sqr1.size)

    def test_flt_x(self):
        with self.assertRaises(TypeError):
            Square(3, 2.2)

    def test_non_x(self):
        with self.assertRaises(TypeError):
            Square(3, None)

    def test_chr_x(self):
        with self.assertRaises(TypeError):
            Square(3, 'a')

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Square(3, "UWU")

    def test_boo_x(self):
        with self.assertRaises(TypeError):
            Square(3, True)

    def test_lst_x(self):
        with self.assertRaises(TypeError):
            Square(3, [2, 2])

    def test_dic_x(self):
        with self.assertRaises(TypeError):
            Square(3, {"size": 1})

    def test_set_x(self):
        with self.assertRaises(TypeError):
            Square(3, {1, 1})

    def test_tup_x(self):
        with self.assertRaises(TypeError):
            Square(3, (1, 1))

    def test_ngv_x(self):
        with self.assertRaises(ValueError):
            Square(3, -3)

    def test_zed_x(self):
        sqr1 = Square(3, 0)
        self.assertEqual(sqr1.x, 0)

if __name__ == '__main__':
    unittest.main()
