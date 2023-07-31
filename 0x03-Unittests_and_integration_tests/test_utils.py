#!/usr/bin/env python3

"""
creating a test access nested map
"""

import unittest
from parameterized import parameterized
import utils
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    creating the test access nested map class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ class to test json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        class Mocked(Mock):
            """a class that inherits from mock"""

            def json(self):
                """ a function to return a json"""
                return test_payload

        with patch("requests.get") as MockedClass:
            MockedClass.return_value = Mocked()
            self.assertEqual(utils.get_json(test_url), test_payload)
