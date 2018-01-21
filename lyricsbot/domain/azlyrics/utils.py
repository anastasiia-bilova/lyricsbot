"""
Tests for custom implementation of built-in Python methods called `lib`.
"""
from string import punctuation

from lyricsbot.lib import join, split


def suitable_azlyrics_url_parameters(url_parameter):
    """
    Test overall split cases.
    """
    # import pdb
    # pdb.set_trace()
    return join(split(url_parameter, ' '), '').lower()


def remove_punctuation_symbols(parameter):
    """
    Test overall split cases.
    """
    return join([el for el in parameter if el not in punctuation], '')
