"""
Tests for custom implementation of built-in Python methods called `lib`.
"""
from lyricsbot.domain.azlyrics.utils import (
    suitable_azlyrics_url_parameters,
    remove_punctuation_symbols,
)

from lyricsbot.domain.azlyrics.config import AZLYRICS_DOWNLOAD_URL


def format_request_song_data_url(author_song, title_song):
    """
    Modify path component of URL.
    """
    author_song = suitable_azlyrics_url_parameters(
        remove_punctuation_symbols(author_song)
    )

    title_song = suitable_azlyrics_url_parameters(
        remove_punctuation_symbols(title_song)
    )

    url = AZLYRICS_DOWNLOAD_URL.format(
        author_song, title_song
    )

    return url
