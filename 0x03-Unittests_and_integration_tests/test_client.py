#!/usr/bin/env python3

"""
testgithuborgclient module
"""

from unittest.mock import patch
from parameterized import parameterized
import utils
import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ unittest class"""
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test TestGithubOrgClient's org method
        Args:
            org (str): organisation's name
        """
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()
