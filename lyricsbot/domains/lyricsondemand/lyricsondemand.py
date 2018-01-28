"""
Get song lyrics via users' data.
"""
import requests
from bs4 import BeautifulSoup

from lyricsbot.domains.lyricsondemand.config import LYRICSONDEMAND_DOWNLOAD_URL
from lyricsbot.domains.lyricsondemand.utils import (
    make_suitable_url_parameters,
    remove_punctuation_symbols,
)


def format_request_data_url(author_song, title_song):
    """
    Modify path components of URL.

    Return an URL link with the suitable url parameters.
    """
    author_song = remove_punctuation_symbols(author_song)
    title_song = remove_punctuation_symbols(title_song)

    formatted_author_song = make_suitable_url_parameters(author_song)
    formatted_title_song = make_suitable_url_parameters(title_song)

    # url for current site needs first letter of author song because of searching by characters
    first_letter_author_song = formatted_author_song[0]

    url = LYRICSONDEMAND_DOWNLOAD_URL.format(
        first_letter_author_song, formatted_author_song, formatted_title_song
    )

    return url


def parse_lyrics(url):
    """
    Parse URL to get song text.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lyrics_raw_content = soup.find_all(attrs={'class': 'lcontent'})

    lyrics_string = ''

    for text in lyrics_raw_content:
        lyrics_string = text.get_text()

    lyrics_without_line_feeds = lyrics_string[4:-4]

    return lyrics_without_line_feeds


def get_song_text(author, title):
    """
    Get song lyrics.
    """
    return parse_lyrics(format_request_data_url(author, title))
