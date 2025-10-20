#!/usr/bin/env python3

"""Function that performs
matrix multiplication"""


def mat_mul(mat1, mat2):
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])

    if col1 != row2:
        return None
    result = []
    for i in range(row1):
        row = []
        """create a matrix filled with 0"""
        for j in range(col2):
            row.append(0)
        result.append(row)
    """Now perform the matrix multiplication"""
    for i in range(row1):
        for j in range(col2):
            dot_prod = []
            for k in range(col1):
                dot_prod.append(mat1[i][k] * mat2[k][j])
            result[i][j] = sum(dot_prod)
    return result
