#!/usr/bin/python3
"""Defines a function that divides a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Parameters:
    - matrix (list of lists): Matrix of integers or floats.
    - div (number): Divisor, should be non-zero integer or float.
    Returns:
    - divided_matrix: elements rounded to 2 decimal places after division.
    Raises:
    - TypeError: If the input matrix is not list of lists of integers/floats,
                 or if each row of matrix does not have same size,
                 or if divisor is not number.
    - ZeroDivisionError: If divisor is equal to zero.
    """

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    if not all(isinstance(rw, list) and all(isinstance(ele, (int, float))
                                            for ele in rw) for rw in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    if any(len(rw) != len(matrix[0]) for rw in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = [[round(ele / div, 2) for ele in rw] for rw in matrix]

    return divided_matrix
