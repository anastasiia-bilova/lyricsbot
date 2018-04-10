"""
Get the song lyrics via users' data from genius.com.
"""
import requests
from bs4 import BeautifulSoup

try:
    from domains.genius.config import GENIUS_DOWNLOAD_URL
    from domains.genius.utils import (
        make_suitable_url_parameters,
        remove_punctuation_symbols,
    )
    from domains.songlyrics.songlyrics import get_song_text_from_songlyrics
# pylint:disable=bare-except
except:  # noqa: E722 # Python 3.5 does not contain `ModuleNotFoundError`
    from lyricsbot.domains.genius.config import GENIUS_DOWNLOAD_URL
    from lyricsbot.domains.genius.utils import (
        make_suitable_url_parameters,
        remove_punctuation_symbols,
    )
    from lyricsbot.domains.songlyrics.songlyrics import get_song_text_from_songlyrics

# if the lyrics of song dont exist on genius.com
LYRICS_DO_NOT_EXIST = 'Sorry, we didn\'t mean for that to happen!'


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

    return full_lyrics_string


def get_song_text_from_genius(author, title):
    """
    Get song lyrics from genius.com.
    """
    complete_text = parse_lyrics(format_request_data_url(author, title))

    if LYRICS_DO_NOT_EXIST in complete_text:
        return get_song_text_from_songlyrics(author, title)

    return complete_text
