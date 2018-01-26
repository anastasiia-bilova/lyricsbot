"""
Getting song lyrics via users' data.
"""
from bs4 import BeautifulSoup

import requests

from lyricsbot.domains.songlyrics.utils import (
    remove_punctuation_symbols,
    suitable_url_parameters
)

from lyricsbot.domains.songlyrics.config import SONGLYRICS_DOWNLOAD_URL


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

    url = SONGLYRICS_DOWNLOAD_URL.format(
        author_song, title_song
    )

    return url


def parse_lyrics(url):
    """
    Parse URL for getting song text.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lyrics_list = [text.get_text() for text in soup.find_all(attrs={'class': 'songLyricsV14 iComment-text'})]

    return '\n'.join(lyrics_list)


def get_song_text(author, title):
    """
    Return full song lyrics.
    """
    return parse_lyrics(format_request_data_url(author, title))
