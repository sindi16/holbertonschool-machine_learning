#!/usr/bin/env python3
"""A script that calculates the shape o matrix"""


def matrix_shape(matrix):
    """Function that calculates the shape of matrix"""
    matrix_shape = []
    while type(matrix) is list:
        matrix_shape.append(len(matrix))
        matrix = matrix[0]
    return matrix_shape
