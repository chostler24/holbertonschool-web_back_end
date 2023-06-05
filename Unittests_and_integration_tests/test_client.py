#!/usr/bin/env python3
"""Module for GitHub Test Client class"""
import client
import unittest
from unittest.mock import patch, PropertyMock
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
        """function tests public repo"""
        mock_payload = [{"name": "Test"}]
        mock_get_json.return_value = mock_payload

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "Test"
            test_class = GithubOrgClient("test")
            self.assertEqual(
                test_class.public_repos(),
                ["Test"]
            )
            mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
