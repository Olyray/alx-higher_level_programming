#!/usr/bin/python3
"""The unittest module for square.py"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(2, id=2)
        s2 = Square(2, id=12)
        s3 = Square(2, 3, 4)
        s4 = Square(2, 3, 4, id=12)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s3.x, 3)
        self.assertEqual(s3.y, 4)
        
    def test_area(self):
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        
    def test_str(self):
        s1 = Square(2, id=4)
        self.assertEqual(str(s1), "[Square] (4) 0/0 - 2")
        
    def test_update(self):
        s1 = Square(2)
        s1.update(12, 2, 3, 4)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_to_dictionary(self):
        s1 = Square(2)
        s1.update(12, 2, 3, 4)
        s1_dict = {'id': 12, 'size': 2, 'x': 3, 'y': 4}
        self.assertEqual(s1.to_dictionary(), s1_dict)

if __name__ == '__main__':
    unittest.main()
