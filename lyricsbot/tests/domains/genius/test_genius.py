"""
Tests to verify the data song with url and parser for genius.com.
"""
import unittest

from ddt import ddt, data, unpack

try:
    from domains.genius.genius import (
        format_request_data_url,
        get_song_text_from_genius,
        parse_lyrics,
    )
    from tests.domains.utils import (
        EXPECTED_KOPECKY_FOR_GENIUS,
        EXPECTED_EMPTYSELF_FOR_GENIUS,
    )
# pylint:disable=bare-except
except:  # noqa: E722 # Python 3.5 does not contain `ModuleNotFoundError`
    from lyricsbot.domains.genius.genius import (
        format_request_data_url,
        get_song_text_from_genius,
        parse_lyrics,
    )
    from lyricsbot.tests.domains.utils import (
        EXPECTED_KOPECKY_FOR_GENIUS,
        EXPECTED_EMPTYSELF_FOR_GENIUS,
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
            'https://genius.com/Kopecky-talk-to-me-lyrics',
        ),
        (
            'Florence + The Machine',
            'Rabbit Heart (Raise It Up)',
            'https://genius.com/Florence-the-machine-rabbit-heart-raise-it-up-lyrics',
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
        Expected: complete song lyrics.
        """
        url = 'https://genius.com/Kopecky-talk-to-me-lyrics'
        result = parse_lyrics(url)

        self.assertEqual(EXPECTED_KOPECKY_FOR_GENIUS, result)

    def test_parse_lyrics_without_text(self):
        """
        Case: link should reproduce the error message, because the song is not available.
        Expected: the message about the unavailability of a song.
        """
        url = 'https://genius.com/Eminem-beautiful-lyrics'
        expected_error = 'The song is not available, sorry.'

        result = parse_lyrics(url)

        self.assertEqual(expected_error, result)

    def test_parse_lyrics_text_exist(self):
        """
        Case: link should reproduce the error message, because the song doesn't exist or entered data without a button.
        Expected: message that the song does not exist.
        """
        url = 'https://genius.com/wewewe-qyqyqy-lyrics'
        expected = u"\n    Sorry, we didn't mean for that to happen!\n  "

        result = parse_lyrics(url)

        self.assertEqual(expected, result)

    @data(
        (
            'Kopecky',
            'Talk To Me',
            EXPECTED_KOPECKY_FOR_GENIUS,
        ),
        (
            'emptyself',
            'artificial light',
            EXPECTED_EMPTYSELF_FOR_GENIUS,
        ),
    )
    @unpack
    def test_get_song_lyrics(self, author, title, expected_result):
        """
        Case: get the complete lyrics song.
        Expected: the complete lyrics.
        """
        result = get_song_text_from_genius(author, title)

        self.assertEqual(expected_result, result)
