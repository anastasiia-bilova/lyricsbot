"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domain.lyricsondemand.utils import (
    remove_punctuation_symbols,
    suitable_url_parameters
)


@ddt
class TestURL(unittest.TestCase):
    """
    Test for verifying removing punctuation symbols.
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
        Case: remove all punctuation symbols in string.
        Expected: string without symbols with spaces.
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
        Case: remove all spaces in string.
        Expected: string without spaces.
        """
        result = suitable_url_parameters(string)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
