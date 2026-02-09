#!/usr/bin/env python3
"""
4-f1_score.py
Calculates F1 score from a confusion matrix
"""


import numpy as np


def f1_score(confusion):
    """
    Returns F1 score per class given a confusion matrix
    """
    # Import the functions from previous tasks
    sensitivity = __import__('1-sensitivity').sensitivity
    precision = __import__('2-precision').precision

    rec = sensitivity(confusion)
    prec = precision(confusion)
    classes = confusion.shape[0]
    f1 = np.zeros(classes,)
    
    # Avoid division by zero
    f1 = 2 * (prec * rec) / (prec + rec + 1e-8)
    return f1
