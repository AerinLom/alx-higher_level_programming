#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if not matrix:
        print()

    else:
        for line in range(len(matrix)):
            for cells in range(len(matrix[line])):
                if cells != len(matrix[line]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[line][cells]), end=endspace)

            print()
