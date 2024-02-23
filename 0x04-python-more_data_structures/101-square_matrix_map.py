#!/usr/bin/python3

# Write a function that computes the square value
# of all integers of a matrix using map
# Your file should be max 3 lines
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y*y, x)), matrix))
