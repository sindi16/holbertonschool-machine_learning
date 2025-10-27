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

            variance = sum((x - self.mean) ** 2 for x in data) / len(data)

            self.stddev = variance ** 0.5

    def z_score(self, x):
        """calculates the z-score of a given x-value"""
        mean = self.mean
        stddev = self.stddev
        z = (x - mean) / stddev
        return z

    def x_value(self, z):
        """calculates the x-value of a given z-score"""
        mean = self.mean
        stddev = self.stddev
        x = (z * stddev) + mean
        return x

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        e = 2.7182818285
        pi = 3.1415926536
        return (1 / (self.stddev * (2 * pi)**0.5)) * \
            e ** (-((x - self.mean)**2) / (2 * self.stddev**2))

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        pi = 3.1415926536

        z = (x - self.mean) / (self.stddev * (2 ** 0.5))

        erf_approx = (
            z
            - (z ** 3) / 3
            + (z ** 5) / 10
            - (z ** 7) / 42
            + (z ** 9) / 216
        )

        erf_approx *= (2 / (pi ** 0.5))

        cdf_value = 0.5 * (1 + erf_approx)
        return cdf_value
