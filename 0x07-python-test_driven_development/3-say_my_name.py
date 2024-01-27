#!/usr/bin/python3
"""
Defines a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a firt and last name

    Parameters:
        first_name (str): The main name to be printed.
        last_name (str, optional): The optional last name.
        Defaults to an empty string.
    """

    if(not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")

    if not first_name:
        raise TypeError("first_name is required")

    if(not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
