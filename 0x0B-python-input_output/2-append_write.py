#!/usr/bin/python3
"""
Contains the function "wrtie_file"
"""


def append_write(filename="", text=""):
    """ overrides the content of the file with the text """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
