#!/usr/bin/python3
"""
Defines a function that reads a text file
"""


def read_file(filename=""):
    """
    Prints text file data to stdout
    """
    with open(filename, encoding="utf-8") as file:
        read_file = file.read()
        print(read_file, end="")
