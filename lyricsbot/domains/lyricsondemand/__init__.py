"""
Init.
"""
from lyricsbot.domains.lyricsondemand.utils import (
    remove_punctuation_symbols,
    suitable_url_parameters
)

from lyricsbot.domains.lyricsondemand.lyricsondemand import (
    format_request_data_url,
    parse_lyrics,
)
