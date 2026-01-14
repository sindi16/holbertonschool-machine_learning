#!/usr/bin/env python3
"""Module that defines a Neuron class."""

import numpy as np


class Neuron:
    """Defines a single neuron performing binary classification."""

    def __init__(self, nx):
        """
        Initialize the neuron.

        Args:
            nx (int): number of input features
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for the weights."""
        return self.__W

    @property
    def b(self):
        """Getter for the bias."""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output."""
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron."""
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """Calculates the cost using logistic regression."""
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(
            Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        )
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neuron's predictions."""
        self.__A = self.forward_prop(X)
        cost = self.cost(Y, self.__A)
        result = np.where(self.__A >= 0.5, 1, 0)
        return result, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        "Calculates one pass of gradient descent on the neuron"
        m = Y.shape[1]

        dW = (1 / m) * np.matmul((A - Y), X.T)
        db = (1 / m) * np.sum(A - Y)
        self.__W = self.__W - alpha * dW
        self.__b = self.__b - alpha * db
