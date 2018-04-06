"""
Helpers for `songlyrics` implementation.
"""
from string import punctuation

try:
    from lib.lib import join, split
# pylint:disable=bare-except
except:  # noqa: E722 # Python 3.5 does not contain `ModuleNotFoundError`
    from lyricsbot.lib.lib import join, split


def make_suitable_url_parameters(url_parameter):
    """
    Return a lowercase string with hyphen.
    """
    return join(split(url_parameter, ' '), '-').lower()


def remove_punctuation_symbols(parameter):
    """
    Remove all punctuation symbols from string.
    """
    string = ''

    if ' + ' in parameter:
        parameter = parameter.replace(' + ', ' ')

    for element in parameter:
        if element not in punctuation:
            string += element

    return string
