#!/usr/bin/python3
"""
Defines a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes data to a UTF-8 text file
    """
    with open(filename, "w", encoding="utf-8") as file:
        written_data = file.write(text)
        return written_data
