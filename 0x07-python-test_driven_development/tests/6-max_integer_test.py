#!/usr/bin/python3
"""Unittest with max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 7]), 7)
        self.assertEqual(max_integer([7, 3, 4, -2]), 7)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7, -3]), -3)

if __name__ == '__main__':
    unittest.main()
