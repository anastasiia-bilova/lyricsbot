"""
Helper for `songlyrics` implementation.
"""
from string import punctuation

from lyricsbot.lib import join, split


def make_suitable_url_parameters(url_parameter):
    """
    Data-in is a string with spaces or without any punctuation symbol.

    Return a string with hyphen and a copy of the string with all the
    cased characters converted to lowercase.
    """
    return join(split(url_parameter, ' '), '-').lower()


def remove_punctuation_symbols(parameter):
    """
    Remove all punctuation symbols from string (author and title song).

    If a punctuation symbol is in the string, remove them.
    Return a string without punctuation symbols.
    """
    string = ''

    if ' + ' in parameter:
        parameter = parameter.replace(' + ', ' ')

    for element in parameter:
        if element not in punctuation:
            string += element

    return string
