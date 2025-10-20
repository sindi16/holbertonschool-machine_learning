#!/usr/bin/env python3
"""Function to concacenate two matrices
    along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):

    if axis == 0:
        if len(mat1[0] != len(mat2[0])):
            return None
        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result
    
    
        







    
