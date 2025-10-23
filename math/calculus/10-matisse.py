#!/usr/bin/env python3
"""A script that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """A function that calculates the derivative of a polynomial"""
    if type(poly) is not list or len(poly) == 0:
        return None

    for coeff in poly:
        if type(coeff) not in (int, float):
            return None

    if len(poly) == 1:
        return [0]

    derivative = []
    for power in range(1, len(poly)):
        derivative.append(poly[power] * power)

    return derivative
