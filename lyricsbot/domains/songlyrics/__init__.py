"""
Init.
"""
from lyricsbot.domain.songlyrics.utils import (
    remove_punctuation_symbols,
    suitable_url_parameters
)

from lyricsbot.domain.songlyrics.songlyrics import (
    format_request_data_url,
    parse_lyrics,
)
