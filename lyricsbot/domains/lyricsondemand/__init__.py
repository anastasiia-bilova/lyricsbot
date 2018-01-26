"""
Init.
"""
from lyricsbot.domain.lyricsondemand.utils import (
    remove_punctuation_symbols,
    suitable_url_parameters
)

from lyricsbot.domain.lyricsondemand.lyricsondemand import (
    format_request_data_url,
    parse_lyrics,
)
