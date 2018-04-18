"""
Tests to verify the data song with url and parser for songlyrics.com.
"""
import unittest

from ddt import ddt, data, unpack

try:
    from domains.songlyrics.songlyrics import (
        format_request_data_url,
        get_song_text_from_songlyrics,
        parse_lyrics,
    )
    from tests.domains.utils import (
        EXPECTED_FLORENCE,
        EXPECTED_KOPECKY_FOR_SONGLYRICS,
    )
# pylint:disable=bare-except
except:  # noqa: E722 # Python 3.5 does not contain `ModuleNotFoundError`
    from lyricsbot.domains.songlyrics.songlyrics import (
        format_request_data_url,
        get_song_text_from_songlyrics,
        parse_lyrics,
    )
    from lyricsbot.tests.domains.utils import (
        EXPECTED_FLORENCE,
        EXPECTED_KOPECKY_FOR_SONGLYRICS,
    )


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

        self.assertEqual(EXPECTED_FLORENCE, result)

    def test_parse_with_large_text(self):
        """
        Case: link should reproduce the error message, because the song is not available.
        Expected: the message about the unavailability of a song.
        """
        url = 'https://genius.com/Eminem-beautiful-lyrics'
        expected = 'Song doesn\'t exist!\nTo get song lyrics tap the press me button.'

        result = parse_lyrics(url)

        self.assertEqual(expected, result)

    def test_parse_lyrics_text_exist(self):
        """
        Case: link should reproduce the error message, because the song doesn't exist or entered data without a button.
        Expected: message that the song does not exist.
        """
        url = 'https://genius.com/wewewe-qyqyqy-lyrics'
        expected = 'Song doesn\'t exist!\nTo get song lyrics tap the press me button.'

        result = parse_lyrics(url)

        self.assertEqual(expected, result)

    @data(
        (
            'Kopecky',
            'Talk To Me',
            EXPECTED_KOPECKY_FOR_SONGLYRICS,
        ),
        (
            'florence + the machine',
            'Rabbit Heart (Raise It Up)',
            EXPECTED_FLORENCE,
        ),
    )
    @unpack
    def test_get_song_lyrics(self, author, title, expected_result):
        """
        Case: get the complete lyrics song.
        Expected: the complete lyrics.
        """
        result = get_song_text_from_songlyrics(author, title)

        self.assertEqual(expected_result, result)
