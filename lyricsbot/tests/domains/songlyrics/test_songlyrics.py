"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domains.songlyrics import (
    format_request_data_url,
    parse_lyrics
)
from lyricsbot.tests.domains.utils import EXPECTED_SONGLYRICS


@ddt
class TestURL(unittest.TestCase):
    """
    Test for verify data song with url and parser.
    """

    @data(
        (
            'Kopecky',
            'Talk To Me',
            'http://www.songlyrics.com/kopecky/talk-to-me-lyrics/',
        ),
        (
            'florence + the machine',
            'Rabbit Heart (Raise It Up)',
            'http://www.songlyrics.com/florence-the-machine/rabbit-heart-raise-it-up-lyrics/',
        ),
    )
    @unpack
    def test_format_request_data_url(self, author_song, title_song, expected_url):
        """
        Case: author and title should be indicated in the link.
        Expected: url with concatenated lowercase characters author and title.
        """
        result = format_request_data_url(author_song, title_song)

        self.assertEqual(expected_url, result)

    def test_parse_lyrics(self):
        """
        Case: get song lyrics thru URL.
        Expected: song lyrics.
        """
        url = 'http://www.songlyrics.com/florence-the-machine/rabbit-heart-raise-it-up-lyrics/'
        result = parse_lyrics(url)
        self.assertEqual(EXPECTED_SONGLYRICS, result)
