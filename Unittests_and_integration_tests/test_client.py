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
        expected_result = {"org": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
