#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    ps_list = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        row_list = [1]
        last_row = ps_list[-1]

        for j in range(len(last_row) - 1):
            row_list.append(last_row[j] + last_row[j+1])
        row_list.append(1)
        ps_list.append(row_list)

    return (ps_list)
