#!/usr/bin/env python3
"""Poisson distribution class."""


class Poisson:
    """Class that represents a Poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Class constructor"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def factorial(self, n):
        """Calculate factorial of n"""
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def exp_neg(self, x, terms=20):
        """Approximate e^-x using Taylor series"""
        result = 0
        for n in range(terms):
            result += ((-x) ** n) / self.factorial(n)
        return result

    def pmf(self, k):
        """Calculates the PMF for a given number of successes k"""
        k = int(k)
        if k < 0:
            return 0
        return (self.lambtha ** k * self.exp_neg(self.lambtha)) / self.factorial(k)

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of successes"""
        k = int(k)
        if k < 0:
            return 0
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return total
