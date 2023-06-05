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

    @patch('client.get_json')
    def test_public_repos_url(self, mock):
        """function tests repo url"""
        test_class = GithubOrgClient("google")
        mock.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        self.assertEqual(
            test_class._public_repos_url,
            mock.return_value.get("repos_url")
        )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload

        client = GithubOrgClient("test_org")
        result = client.public_repos()

        expected_result = ["repo1", "repo2"]
        self.assertEqual(result, expected_result)

        mock_get_json.assert_called_once_with(
            "https://api.github.com/repos/test_org/repos")


if __name__ == '__main__':
    unittest.main()
