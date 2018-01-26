"""
Init.
"""
from lyricsbot.domains.songlyrics.utils import (
    remove_punctuation_symbols,
    suitable_url_parameters
)

from lyricsbot.domains.songlyrics.songlyrics import (
    format_request_data_url,
    parse_lyrics,
)
