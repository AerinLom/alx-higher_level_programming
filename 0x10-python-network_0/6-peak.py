#!/usr/bin/python3
"""
Algorithm to find peaK in list of integers
"""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers:
        sorted_list = sorted(list_of_integers, reverse=True)
        return sorted_list[0] 
