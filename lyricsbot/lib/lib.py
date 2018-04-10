"""
Custom implementation of built-in Python methods.
"""


def join(sequence, separator):
    """
    Return a string concatenation with separator between elements.
    """
    string = ''

    for letter in sequence:
        string += letter + separator

    if separator == '':
        return string

    return string[:-1]


def split(string, separator):
    """
    Return a list of the words in the string, using separator as the delimiter.
    """
    if separator == '':
        raise ValueError('Empty separator')

    if separator is None:
        separator = ' '

    sequence, word = [], ''

    string += separator

    for letter in string:
        if letter is not separator:
            word += letter
        else:
            sequence.append(word)
            word = ''

    return sequence
