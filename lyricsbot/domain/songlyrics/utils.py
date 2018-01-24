"""
Helper.
"""
from string import punctuation

from lyricsbot.lib import join, split


def suitable_url_parameters(url_parameter):
    """
    Data-in is a string with spaces or without any punctuation symbol.


    Return a string with hyphen.
    """
    return join(split(url_parameter, ' '), '-').lower()


def remove_punctuation_symbols(parameter):
    """
    Remove all punctuation symbols from string (author and title song).


    If a string is 'Florence + The Machine', slicing the string to needed len.
    If the punctuation symbol is in the string, remove them.
    Return a string without punctuation symbols.
    """
    string = ''
    if parameter == 'Florence + The Machine' or parameter == 'florence + the machine':
        string = parameter[:9] + parameter[11:]
        return string
    for element in parameter:
        if element not in punctuation:
            string += element

    return string
