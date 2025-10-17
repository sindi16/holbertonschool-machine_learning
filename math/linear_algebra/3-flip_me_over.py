#!/usr/bin/env python3
"""A function that returns the transpose of a 2D matrix."""


def matrix_transpose(matrix):
    """
    Computes the transpose of a 2D matrix.

    Args:
        matrix: A list of lists representing the 2D matrix.

    Returns:
        A new list of lists representing the transposed matrix.
    """
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the transposed matrix with swapped dimensions (cols x rows)
    # The list comprehension is concise and idiomatic Python for initialization
    transposed = [[0] * rows for _ in range(cols)]

    # Iterate through the original matrix and swap indices
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
