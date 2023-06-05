#!/usr/bin/env python3
"""Module for GitHub Test Client class"""
import client
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """declaration of class TestGithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """function tests that GitHubOrgClient returns correct value"""
        mock_get_json.return_value = {"payload": True}
        test_class = GithubOrgClient(org_name)
        self.assertEqual(test_class.org, mock_get_json.return_value)
        mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
