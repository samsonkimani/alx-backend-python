#!/usr/bin/env python3

"""
creating a test access nested map
"""

import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except (TypeError, KeyError):
        return None
    pass


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
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
