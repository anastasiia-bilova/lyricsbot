"""
Tests to verify the removal of punctuation characters for genius.com URLs.
"""
import unittest

from ddt import ddt, data, unpack

try:
    from domains.genius.utils import (
        make_suitable_url_parameters,
        remove_punctuation_symbols,
    )
# pylint:disable=bare-except
except:  # noqa: E722 # Python 3.5 does not contain `ModuleNotFoundError`
    from lyricsbot.domains.genius.utils import (
        make_suitable_url_parameters,
        remove_punctuation_symbols,
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
        Case: should be removed all punctuation symbols in author and title.
        Expected: author and title without symbols with spaces.
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
        Case: replace spaces with hyphen in author and title, and formatted there in lowercase.
        Expected: lowercase string with hyphen.
        """
        result = make_suitable_url_parameters(string)

        self.assertEqual(expected, result)
