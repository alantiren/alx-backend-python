#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test org method of GithubOrgClient class.
        """
        mock_payload = {"org_name": org_name}
        mock_get_json.return_value = mock_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(result, mock_payload)

    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json, mock_public_repos_url):
        """
        Test _public_repos_url property of GithubOrgClient class.
        """
        mock_payload = {"repos_url": "http://example.com/repos"}
        mock_get_json.return_value = mock_payload

        client = GithubOrgClient("example")
        result = client._public_repos_url

        mock_get_json.assert_called_once_with(client.ORG_URL.format(org="example"))
        self.assertEqual(result, "http://example.com/repos")

if __name__ == '__main__':
    unittest.main()
