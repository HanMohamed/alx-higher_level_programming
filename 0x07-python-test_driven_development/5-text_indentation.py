#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    There should be no space at the beginning or
    at the end of each printed line
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print()
            print()
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
