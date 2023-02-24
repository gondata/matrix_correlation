# Stock Price Analysis

This code downloads historical stock price data for a list of tickers and generates two visualizations:

1. A line plot showing the performance of each ticker over time.
2. A heatmap showing the correlation between the daily returns of each ticker.

## Prerequisites

- Python 3.
- Required packages: numpy, pandas, yfinance, matplotlib, seaborn, pandas_datareader.

## Installation

1. Clone or download the repository.
2. Install the required packages: **`pip install numpy pandas yfinance matplotlib seaborn pandas_datareader`**.

## Usage

1. Open **`stock_price_analysis.ipynb`** in Jupyter Notebook or your preferred Python environment.
2. Run the code in the notebook.

## Customization

- You can customize the list of **`tickers`** by editing the tickers variable in the code.
- You can adjust the start and end dates for the analysis by editing the **`startdate`** and **`enddate`** variables in the code.
- You can modify the size of the plot by editing the **`figsize`** parameter in the **`plt.figure`** function call.
