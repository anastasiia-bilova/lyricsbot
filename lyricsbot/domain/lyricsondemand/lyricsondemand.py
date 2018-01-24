"""
Getting song lyrics via users' data.
"""
from bs4 import BeautifulSoup

import requests

from lyricsbot.domain.lyricsondemand.utils import (
    remove_punctuation_symbols,
    suitable_url_parameters
)

from lyricsbot.domain.lyricsondemand.config import LYRICSONDEMAND_DOWNLOAD_URL


def format_request_data_url(author_song, title_song):
    """
    Modify path components of URL.
    Return an URL link with the right data.
    """
    author_song = suitable_url_parameters(
        remove_punctuation_symbols(author_song)
    )

    title_song = suitable_url_parameters(
        remove_punctuation_symbols(title_song)
    )

    url = LYRICSONDEMAND_DOWNLOAD_URL.format(
        author_song[0], author_song, title_song
    )

    return url


def parse_lyrics(url):
    """
    Parse URL for getting song text.
    Return full song lyrics.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lyrics_string = ''
    for text in soup.find_all(attrs={'class': 'lcontent'}):
        lyrics_string = text.get_text()

    return lyrics_string[4:-4]


def get_song_text(author, title):
    """
    Getting song lyrics.
    Return full song lyrics.
    """
    return parse_lyrics(format_request_data_url(author, title))
