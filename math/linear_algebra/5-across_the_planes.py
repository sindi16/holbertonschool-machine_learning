#!/usr/bin/env python3
"""Function of the addition of two matrices 
    element-wise.
"""


def add_matrices2D(mat1, mat2): 
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    
    result = []
    for i in range(len(mat1)):
        add = []
        for j in range(len(mat1[0])):
            add.append(mat1[i][j] + mat2[i][j])
        result.append(add)

    return result

