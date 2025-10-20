#!/usr/bin/env python3
"""function that calculates \sum_{i=1}^{n} i^2:"""


def summation_i_squared(n):
    """Return the integer value of the sum"""
    if type(n) is not int:
        return None
    result = n**3/3 + n**2/2 + n/6
