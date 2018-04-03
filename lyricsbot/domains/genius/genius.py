"""
Get song lyrics via users' data.
"""
import requests
from bs4 import BeautifulSoup

from lyricsbot.domains.genius.config import GENIUS_DOWNLOAD_URL
from lyricsbot.domains.genius.utils import (
    make_suitable_url_parameters,
    remove_punctuation_symbols,
)

# if user ask lyrics without 'Press me!' button
LYRICS_WITHOUT_PRESSME_BUTTON = 'Sorry, we didn\'t mean for that to happen!'


def format_request_data_url(author_song, title_song):
    """
    Modify path components of URL.
    """
    author_song = remove_punctuation_symbols(author_song)
    title_song = remove_punctuation_symbols(title_song)

    formatted_author_song = make_suitable_url_parameters(author_song)
    formatted_title_song = make_suitable_url_parameters(title_song)

    # url for current site needs author song with only its first character capitalized
    capitalize_author_song = formatted_author_song.capitalize()

    url = GENIUS_DOWNLOAD_URL.format(
        capitalize_author_song, formatted_title_song
    )

    return url


def parse_lyrics(url):
    """
    Parse URL to get song text.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    full_lyrics_string = soup.find('p').get_text()

    # if the lyrics are more than 3000 characters, then it is too large for telegram message
    if len(full_lyrics_string) > 3000:
        return 'The song is not available, sorry.'

    if LYRICS_WITHOUT_PRESSME_BUTTON in full_lyrics_string:
        full_lyrics_string = 'To get song lyrics tap the press me button.'

    return full_lyrics_string


def get_song_text_from_genius(author, title):
    """
    Get song lyrics.
    """
    return parse_lyrics(format_request_data_url(author, title))
