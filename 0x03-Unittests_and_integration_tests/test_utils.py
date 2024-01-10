#!/usr/bin/env python3
"""
Unit tests for utils module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map with various inputs.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """
        Test access_nested_map with inputs expected to raise exceptions.
        """
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """
    Test cases for get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Test get_json with various inputs.
        """
        mock_json = MagicMock(return_value=test_payload)
        mock_requests_get.return_value.json = mock_json

        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """
    Test cases for memoize decorator.
    """

    class TestClass:
        """
        Test class for memoize decorator.
        """

        def a_method(self):
            """
            Sample method.
            """
            return 42

        @memoize
        def a_property(self):
            """
            Sample property using memoize decorator.
            """
            return s
