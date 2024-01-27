#!/usr/bin/python3

"""
Defines a function that indents texts
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each character: ., ? and :

    Parameters:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not of type string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_flags = [".", "?", ":"]
    sen_lines = text.split("\n")
    for line in sen_lines:
        line = line.strip()
        if line:
            for char in line:
                print(char, end="")
                if char in punctuation_flags:
                    print("\n\n", end="")
