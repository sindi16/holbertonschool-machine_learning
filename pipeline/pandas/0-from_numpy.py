#!/usr/bin/env python3
"""create a pd.DataFrame from a np.ndarray"""


import pandas as pd
import string


def from_numpy(array):
    """function that takes an np.ndarray and return a pd.dataframe."""
    n_cols = array.shape[1]
    columns = list(string.ascii_uppercase[:n_cols])

    df = pd.DataFrame(array, columns=columns)
    return df
