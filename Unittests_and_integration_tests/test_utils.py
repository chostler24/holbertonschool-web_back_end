#!/usr/bin/env python3
"""Module for class TestAccessNestedMap"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for utilizing access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Unittest module"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
