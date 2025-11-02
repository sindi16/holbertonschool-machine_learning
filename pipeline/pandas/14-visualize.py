#!/usr/bin/env python3
"""Visualize Coinbase Bitcoin daily data from 2017 onward."""

import matplotlib.pyplot as plt
import pandas as pd

from_file = __import__('2-from_file').from_file


df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df = df.drop(columns=['Weighted_Price'])

df = df.rename(columns={'Timestamp': 'Date'})

df['Date'] = pd.to_datetime(df['Date'], unit='s')

df = df.set_index('Date')



df.plot(subplots=True, figsize=(10, 10),
        title='Bitcoin Daily Data (2017 and Beyond)')
plt.tight_layout()
plt.show()
