#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares_matrix = [[x ** 2 for x in row] for row in matrix]
    return squares_matrix
