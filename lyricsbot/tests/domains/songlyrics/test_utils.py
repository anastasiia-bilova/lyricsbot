"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domains.songlyrics.utils import (
    remove_punctuation_symbols,
    make_suitable_url_parameters
)


@ddt
class TestURL(unittest.TestCase):
    """
    Test for verifying removing punctuation symbols.
    """

    @data(
        ('Childish Gambino', 'Childish Gambino'),
        ('Redbone', 'Redbone'),
        ('Florence + The Machine', 'Florence The Machine'),
        ('Rabbit Heart (Raise It Up)', 'Rabbit Heart Raise It Up'),
    )
    @unpack
    def test_remove_punctuation_symbols(self, string, expected):
        """
        Case: remove all punctuation symbols in string.
        Expected: string without symbols with spaces.
        """
        result = remove_punctuation_symbols(string)
        self.assertEqual(expected, result)

    @data(
        ('Florence The Machine', 'florence-the-machine'),
        ('Rabbit Heart Raise It Up', 'rabbit-heart-raise-it-up'),
    )
    @unpack
    def test_suitable_url_parameters(self, string, expected):
        """
        Case: remove all spaces in string.
        Expected: string with hyphen.
        """
        result = make_suitable_url_parameters(string)
        self.assertEqual(expected, result)
