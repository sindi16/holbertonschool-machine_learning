#!/usr/bin/env python3
"""Performs element-wise addition, subtraction, multiplication, and division
on two NumPy arrays or between a NumPy array and a scalar."""


def np_elementwise(mat1, mat2):
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
