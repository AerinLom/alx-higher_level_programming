#!/usr/bin/python3
"""
Algorithm to find peaK in list of integers
"""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers:
        return max(list_of_integers)
