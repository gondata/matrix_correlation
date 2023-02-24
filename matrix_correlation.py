# First of all we have to import the libraries that we are going to use

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as pdr

yf.pdr_override()

# Then we have to download the data

tickers = ['MSFT', 'UNP', 'GOOG', 'IBM', '^GSPC', 'TSLA', 'AAPL', 'AMZN', 'V', 'BBBY', 'MCD', 'QQQ', 'IWM']
startdate = '2015-01-01'
enddate = '2023-02-24'

data = pdr.get_data_yahoo(tickers, start=startdate, end=enddate)['Adj Close']

# Variables

returns = data.pct_change()[1:] # We skip 1 period

# Graphs

fig = plt.figure(figsize=(20, 8)) # Correlation matrix

ax1 = fig.add_subplot(121) # 121: Graph on the left, on the top.
ax2= fig.add_subplot(122) # 122: Graph on the right, on the top.

# Bucle for graph 1

for stk in tickers:
    ax1.plot(data[stk]/data[stk][0]*100, label=stk)
    ax1.legend()

# Heatmap for graph 2

sns.heatmap(returns.corr(), annot=True, cmap="YlGnBu", ax=ax2)
plt.show()