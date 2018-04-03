"""
Tests for custom implementation of built-in Python methods called `lib`.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.lib.lib import join, split


@ddt
class TestLib(unittest.TestCase):
    """
    Test for custom implementation built-in Python methods.
    """

    @data(
        (' ', 'Game of Thrones'),
        ('_', 'Game_of_Thrones'),
        ('', 'GameofThrones'),
    )
    @unpack
    def test_join(self, join_separator, expected):
        """
        Test overall join cases.
        """
        sequence_to_join = ['Game', 'of', 'Thrones']
        response = join(sequence_to_join, join_separator)

        self.assertEqual(expected, response)

    @data(
        ('Game of Thrones', ' '),
        ('Game_of_Thrones', '_'),
    )
    @unpack
    def test_split(self, string_to_split, symbol_by_split):
        """
        Test overall split cases.
        """
        expected = ['Game', 'of', 'Thrones']
        response = split(string_to_split, symbol_by_split)

        self.assertEqual(expected, response)

    def test_split_empty_symbol(self):
        """
        Case: split by empty symbol separator.
        Expected: ValueError raise.
        """
        string_to_split, symbol_by_split = 'GameofThrones', ''
        expected_error = ValueError

        with self.assertRaises(expected_error):
            split(string_to_split, symbol_by_split)

    def test_split_none(self):
        """
        Case: split by None separator.
        Expected: split works with None separator as like space symbol.
        """
        string_to_split, symbol_by_split = 'GameofThrones', None
        expected = ['GameofThrones']

        response = split(string_to_split, symbol_by_split)

        self.assertEqual(expected, response)
