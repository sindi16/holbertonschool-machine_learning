#!/usr/bin/env python3
"""
Save and load model functions
"""

import tensorflow.keras as K


def save_model(network, filename):
    """
    Save an entire model.

    Args:
        network: The model to save.
        filename: The file path to save the model to.
    """
    network.save(filename)


def load_model(filename):
    """
    Load an entire model.

    Args:
        filename: The file path to load the model from.

    Returns:
        The loaded model.
    """
    return K.models.load_model(filename)
