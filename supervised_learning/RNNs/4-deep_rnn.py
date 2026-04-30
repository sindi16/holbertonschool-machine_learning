#!/usr/bin/env python3
"""Deep RNN Module"""
import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """Performs forward propagation for a deep RNN"""

    t, m, _ = X.shape
    num_layers, _, h = h_0.shape

    H = np.zeros((t + 1, num_layers, m, h))
    H[0] = h_0

    o = rnn_cells[-1].by.shape[1]
    Y = np.zeros((t, m, o))

    for i in range(t):
        x_t = X[i]

        for layer, rnn_cell in enumerate(rnn_cells):
            h_prev = H[i, layer]

            h_next, y = rnn_cell.forward(h_prev, x_t)
            H[i + 1, layer] = h_next

            x_t = h_next

        Y[i] = y

    return H, Y
