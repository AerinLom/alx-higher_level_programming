#!/usr/bin/python3
"""
This module inherits from list
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints a list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
