#!/usr/bin/env python3
"""A function that Removes any entries
 where Close has NaN values"""


def prune(df):
    """Removes any entries where Close has NaN values"""
    df = df.dropna(subset=['Close'])

    return df
