#!/usr/bin/env python3
"""Module for class TestAccessNestedMap"""
import unittest
from unittest.mock import mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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
    def test_get_json(self, test_url, test_payload, mock_get):
        """get json method"""
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

if __name__ == '__main__':
    unittest.main()
