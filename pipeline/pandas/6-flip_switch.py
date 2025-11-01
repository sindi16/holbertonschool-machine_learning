#!/usr/bin/env python3
"""Transposes the sorted dataframe
and returns the transformed df"""


def flip_switch(df):
    """Sorts the data in reverse chronological order"""
    df = df.sort_values(by='Timestamp', ascending=False).T

    return df
