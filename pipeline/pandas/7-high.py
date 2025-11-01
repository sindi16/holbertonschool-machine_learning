#!/usr/bin/env python3
"""A function that takes a pd.DataFrame"""

import pandas as pd


def high(df):
    """Sorts it by the High price in descending order."""
    df = df.sort_values(by='High', ascending=False)

    return df
