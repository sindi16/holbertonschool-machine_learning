#!/usr/bin/env python3
"""Function that concatenates two matrices along a specific axis."""


def np_cat(mat1, mat2, axis=0):
    import numpy as np
    return np.concatenate((mat1, mat2), axis=axis)
