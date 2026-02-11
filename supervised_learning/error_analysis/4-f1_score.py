#!/usr/bin/env python3
"""
    F1 score computation
"""
import numpy as np
get_recall = __import__('1-sensitivity').sensitivity
get_precision = __import__('2-precision').precision


def compute_f1(conf_matrix):
    """
    Calculates the F1 score for each class using a confusion matrix

    :param conf_matrix: ndarray of shape (num_classes, num_classes)
    :return: ndarray of shape (num_classes,) containing F1 scores
    """

    # Total number of classes
    num_classes = conf_matrix.shape[0]

    # Initialize array to store F1 scores
    f1_scores = np.zeros(num_classes)

    # Compute precision and recall for all classes
    precisions = get_precision(conf_matrix)
    recalls = get_recall(conf_matrix)

    # Compute F1 score per class
    for class_idx in range(num_classes):
        f1_scores[class_idx] = (
            2 * precisions[class_idx] * recalls[class_idx]
        ) / (
            precisions[class_idx] + recalls[class_idx]
        )

    return f1_scores
