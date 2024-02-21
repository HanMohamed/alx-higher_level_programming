#!/usr/bin/python3

# Write a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    sqr_matrix = [list(map(lambda x: x * x, row)) for row in matrix]

    return sqr_matrix
