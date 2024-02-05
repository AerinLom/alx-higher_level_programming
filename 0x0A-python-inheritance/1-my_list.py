#!/usr/bin/python3
"""
This module inherits from list
"""


class MyList(list):
    """
    Conducts a sorted sub class list to be printed
    """
    def print_sorted(self):
        """
        Prints a list in ascending order
        """
	list_sorted = sorted(self)
        print(list_sorted)
