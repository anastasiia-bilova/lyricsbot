"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domains.lyricsondemand.utils import (
    make_suitable_url_parameters,
    remove_punctuation_symbols,
)


@ddt
class TestURL(unittest.TestCase):
    """
    Test for verify removing punctuation symbols.
    """

    @data(
        ('Childish Gambino', 'Childish Gambino'),
        ('Redbone', 'Redbone'),
        ('Florence + The Machine', 'Florence and The Machine'),
        ('Rabbit Heart (Raise It Up)', 'Rabbit Heart Raise It Up'),
    )
    @unpack
    def test_remove_punctuation_symbols(self, string, expected):
        """
        Case: should be removed all punctuation symbols in author and title.
        Expected: author and title without symbols with spaces.
        """
        result = remove_punctuation_symbols(string)
        self.assertEqual(expected, result)

    @data(
        ('Florence  The Machine', 'florencethemachine'),
        ('Rabbit Heart Raise It Up', 'rabbitheartraiseitup'),
    )
    @unpack
    def test_suitable_url_parameters(self, string, expected):
        """
        Case: remove all spaces in author and title, and formatted there in lowercase.
        Expected: lowercase strings without spaces.
        """
        result = make_suitable_url_parameters(string)
        self.assertEqual(expected, result)
