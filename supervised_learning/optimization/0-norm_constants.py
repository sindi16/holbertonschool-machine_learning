#!/usr/bin/env python3
"""
Calculates the mean and standard deviation of a dataset."""


import numpy as np


def normalization_constants(X):
    """
    Calculates the mean and standard deviation of a dataset.

    Args:
        X (numpy.ndarray): The input data of shape (m, n).
    Returns:
        m (numpy.ndarray): The mean of each feature.
        s (numpy.ndarray): The standard deviation of each feature.
    """
    m = np.mean(X, axis=0)
    s = np.std(X, axis=0)
    return m, s
