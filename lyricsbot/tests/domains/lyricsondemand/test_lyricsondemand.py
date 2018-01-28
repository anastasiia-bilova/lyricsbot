"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domains.lyricsondemand import (
    format_request_data_url,
    parse_lyrics
)
from lyricsbot.tests.domains.utils import EXPECTED_LYRICSONDEMAND


@ddt
class TestURL(unittest.TestCase):
    """
    Test for verify data song with url and parser.
    """

    @data(
        (
            'Childish Gambino',
            'Redbone',
            'https://www.lyricsondemand.com/c/childishgambinolyrics/redbonelyrics.html',
        ),
        (
            'Florence + The Machine',
            'Rabbit Heart (raise it up)',
            'https://www.lyricsondemand.com/f/florenceandthemachinelyrics/rabbitheartraiseituplyrics.html',
        ),
    )
    @unpack
    def test_format_request_data_url(self, author_song, title_song, expected_url):
        """
        Case: url with right data.
        Expected: right url with modifying data.
        """
        result = format_request_data_url(author_song, title_song)

        self.assertEqual(expected_url, result)

    def test_parse_lyrics(self):
        """
        Case: get song lyrics.
        Expected: song lyrics.
        """
        url = 'https://www.lyricsondemand.com/c/childishgambinolyrics/redbonelyrics.html'
        result = parse_lyrics(url)
        self.assertEqual(EXPECTED_LYRICSONDEMAND, result)
