"""
Helpers for `lyricsondemand` implementation.
"""
from string import punctuation

from lyricsbot.lib.lib import join, split


def make_suitable_url_parameters(url_parameter):
    """
    Return a lowercase string without spaces.
    """
    return join(split(url_parameter, ' '), '').lower()


def remove_punctuation_symbols(parameter):
    """
    Remove all punctuation symbols from string.
    """
    string = ''

    if ' + ' in parameter:
        parameter = parameter.replace(' + ', ' and ')

    for element in parameter:
        if element not in punctuation:
            string += element

    return string
