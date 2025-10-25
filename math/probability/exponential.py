#!/usr/bin/env python3
"""Represents an exponential distribution."""


class Exponential:
    """Class that represents an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Class constructor."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            self.lambtha = float(1 / mean)

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period"""
        if x < 0:
            return 0
        y = self.lambtha * x
        term = 1.0
        exp_approx = 1.0
        for n in range(1, 50):
            term *= -y / n
            exp_approx += term
        return self.lambtha * exp_approx
