#!/usr/bin/python3
"""
Defines a function that appends a string
"""


def append_write(filename="", text=""):
    """
    Appends string at end of text file, returns characters added
    """
    with open(filename, "a", encoding="utf-8") as append_f:
        appended_text = append_f.write(text)
        return appended_text
