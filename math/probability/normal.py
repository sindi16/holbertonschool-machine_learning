#!/usr/bin/env python3
"""representing a normal distribution"""

class Normal:
    """Creating normal class"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Creating the constructor of the class."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)

            variance = sum((x - self.mean) ** 2)
