import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from data_fetcher import get_ticker_data
from statsmodels.tsa.vector_ar.vecm import coint_johansen

#Johansen Cointegration Test (up to 12 cointegration )

# Define the stock pairs
stock_pairs = [('AAPL', 'AMZN'), ('MSFT', 'AAPL'), ('AMZN', 'MSFT')] #PICK DIFFERENT STOCK PRICES

# Define the date range
start_date = '2024-01-08'
end_date = '2025-1-08'

# Function to perform Pantula Principle-based cointegration test
def pantula_principle(data, det_order=0, k_ar_diff=1):
    result = coint_johansen(data, det_order, k_ar_diff)
    trace_stats = result.lr1  # Trace statistics
    critical_values = result.cvt[:, 1]  # 5% critical values

    # Pantula principle: start from r=0, stop when trace < critical
    rank = 0
    for i in range(len(trace_stats)):
        print(trace_stats[i], critical_values[i])
        if trace_stats[i] > critical_values[i]:
            rank += 1
        else:
            break
    return rank

def coint_pairs():
    coint_pairs=[]
    data_list=[]
    # Loop through each pair and apply Pantula strategy
    for idx, (stock1, stock2) in enumerate(stock_pairs, 1):
        tickers = [stock1, stock2]

        # Download adjusted close prices
        data = yf.download(tickers, start=start_date, end=end_date)['Close'].dropna()

        # Apply Pantula principle

        rank = pantula_principle(data)
        
        # Interpret results
        if rank >= 1:
            coint_pairs.append([stock1, stock2])
            data_list.append(data)
            
    return coint_pairs, data_list
        

output, out = coint_pairs()
print(output)