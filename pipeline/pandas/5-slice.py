#!/usr/bin/env python3
"""Slice the DataFrame along the columns High, Low, Close, & Volume_BTC,
   taking every 60th row"""


import pandas as pd


def slice(df):
    """Extracts the columns High, Low, Close, and Volume_BTC"""
    df = df.loc[::60, ['High', 'Low', 'Close', 'Volume_(BTC)']]

    return df
