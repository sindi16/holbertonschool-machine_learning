#!/usr/bin/env python3
"""A function for adding two arrays element-wise"""


def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None  # stop the function if lengths differ
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result   # return the final result
