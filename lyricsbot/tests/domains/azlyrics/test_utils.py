"""
Tests for custom implementation of built-in Python methods called `lib`.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domain.azlyrics.utils import (
    remove_punctuation_symbols,
    suitable_azlyrics_url_parameters,
)


@ddt
class TestURL(unittest.TestCase):
    """
    Test overall split cases.
    """

    @data(
        ('Florence + The Machine', 'Florence  The Machine'),
        ('Rabbit Heart (Raise It Up)', 'Rabbit Heart Raise It Up'),
    )
    @unpack
    def test_remove_punctuation_symbols(self, string, expected):
        """
        Verify the URL format.
        """
        result = remove_punctuation_symbols(string)
        self.assertEqual(expected, result)

    @data(
        ('Florence  The Machine', 'florencethemachine'),
        ('Rabbit Heart Raise It Up', 'rabbitheartraiseitup'),
    )
    @unpack
    def test_suitable_azlyrics_url_parameters(self, string, expected):
        """
        Verify the URL format.
        """
        result = suitable_azlyrics_url_parameters(string)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
