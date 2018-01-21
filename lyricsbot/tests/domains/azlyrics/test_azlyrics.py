"""
Tests for custom implementation of built-in Python methods called `lib`.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domain.azlyrics.azlyrics import format_request_song_data_url


@ddt
class TestURL(unittest.TestCase):
    """
    Test overall split cases.
    """

    @data(
        (
            'Childish Gambino',
            'Redbone',
            'https://www.azlyrics.com/lyrics/childishgambino/redbone.html',
        ),
        (
            'KOPECKY',
            'Talk To Me',
            'https://www.azlyrics.com/lyrics/kopecky/talktome.html',
        ),
        (
            'Florence + The Machine',
            'Rabbit Heart (Raise It Up)',
            'https://www.azlyrics.com/lyrics/florencethemachine/rabbitheartraiseitup.html',
        ),
    )
    @unpack
    def test_format_request_song_data_url(self, author_song, title_song, expected_url):
        """
        Verify the URL format.
        """
        result = format_request_song_data_url(author_song, title_song)

        self.assertEqual(expected_url, result)


if __name__ == '__main__':
    unittest.main()
