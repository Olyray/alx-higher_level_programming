#!/usr/bin/python3
"""unittest module for Rectangle class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(2, 4, id=2)
        r2 = Rectangle(2, 4, id=12)
        r3 = Rectangle(2, 4, 3, 2)
        r4 = Rectangle(2, 4, 3, 2, id=12)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 2)

    def test_area(self):
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)

    def test_str(self):
        r1 = Rectangle(2, 4, id=5)
        self.assertEqual(str(r1), "[Rectangle] (5) 0/0 - 2/4")

    def test_update(self):
        r1 = Rectangle(2, 4)
        r1.update(12, 2, 3, 4, 5)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_to_dictionary(self):
        r1 = Rectangle(2, 4)
        r1.update(12, 2, 3, 4, 5)
        r1_dict = {"id": 12, "width": 2, "height": 3, "x": 4, "y": 5}
        self.assertEqual(r1.to_dictionary(), r1_dict)


if __name__ == "__main__":
    unittest.main()
