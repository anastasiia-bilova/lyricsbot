"""
Get song lyrics via users' data.
"""
import requests
from bs4 import BeautifulSoup

from lyricsbot.domains.songlyrics.config import SONGLYRICS_DOWNLOAD_URL
from lyricsbot.domains.songlyrics.utils import (
    make_suitable_url_parameters,
    remove_punctuation_symbols,
)


def format_request_data_url(author_song, title_song):
    """
    Modify path components of URL.
    """
    author_song = remove_punctuation_symbols(author_song)
    title_song = remove_punctuation_symbols(title_song)

    formatted_author_song = make_suitable_url_parameters(author_song)
    formatted_title_song = make_suitable_url_parameters(title_song)

    url = SONGLYRICS_DOWNLOAD_URL.format(
        formatted_author_song, formatted_title_song
    )

    return url


def parse_lyrics(url):
    """
    Parse URL to get song text.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lyrics_raw_content = soup.find_all(attrs={'class': 'songLyricsV14 iComment-text'})

    lyrics_as_list = [text.get_text() for text in lyrics_raw_content]

    full_lyrics_string = '\n'.join(lyrics_as_list)

    return full_lyrics_string


def get_song_text_from_songlyrics(author, title):
    """
    Get song lyrics.
    """
    return parse_lyrics(format_request_data_url(author, title))
