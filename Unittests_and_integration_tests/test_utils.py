#!/usr/bin/env python3
"""Module for class TestAccessNestedMap"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Unittest module test_access_nested_map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Unittest module test_access_nested_map_exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """TestGetJson class declaration"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Method for testing JSON"""
        mock = Mock()
        mock.json.return_value = payload
        with patch("requests.get", return_value=mock):
            self.assertEqual(get_json(url), payload)
            mock.json.assert_called_once()

class TestMemoize(unittest.TestCase):
    """declaration of class TestMemoize"""
    def test_memoize(self):
        """function tests memoization"""
        class TestClass:
            """Testing class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_inst = TestClass()
        with patch.object(test_inst, "a_method") as mock:
            mock.return_value = 42
            test_inst.a_property
            test_inst.a_property
            mock.assert_called_once()

if __name__ == '__main__':
    unittest.main()
