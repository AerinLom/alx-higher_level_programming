#!/usr/bin/python3
"""
Defines a function that returns a matrix representing Pascal’s triangle
"""


def pascal_triangle(n):
    """
    Definition of Pascal's Triangle of n.
    """
    if n <= 0:
        return []

    pasc_tri = []
    for current_row_index in range(n):
        current_row = [1] * (current_row_index + 1)
        if current_row_index > 1:
            for j in range(1, current_row_index):
                current_row[j] = (pasc_tri[current_row_index - 1]
                                  [j - 1] + pasc_tri[current_row_index - 1][j])
        pasc_tri.append(current_row)

    return pasc_tri
