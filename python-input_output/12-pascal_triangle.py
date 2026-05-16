#!/usr/bin/python3
"""This module provides a function to generate Pascal's Triangle up to n rows.

The module allows computational analysis of binomial coefficients in a grid.
"""


def pascal_triangle(n):
    """Generates a list of lists of integers representing Pascal's triangle of n.

    Returns an empty list if n is less than or equal to zero.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
