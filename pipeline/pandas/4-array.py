#!/usr/bin/env python3
"""A function that takes a pd.DataFrame as input """


def array(df):
    """df is a pd.DataFrame containing columns named High and Close"""
    DF = df.loc[:, ['High', 'Close']].tail(10).to_numpy()

    return DF
