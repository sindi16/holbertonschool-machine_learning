#!/usr/bin/env python3
"""Function to concatenate two matrices
along a specific axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Function that concatenates two matrices along a specific axis"""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = []
        for i in range(len(mat1)):
            new_row = mat1[i] + mat2[i]
            result.append(new_row)
        return result

    else:
        return None
