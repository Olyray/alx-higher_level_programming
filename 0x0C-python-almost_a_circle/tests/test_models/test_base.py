#!/usr/bin/python3
"""Defines unittests for base.py
Unittest classes:
    TestBase
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        b2 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)

    def test_to_json_string(self):
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_dicts, [{"id": 1}, {"id": 2}])

if __name__ == "__main__":
    unittest.main()
