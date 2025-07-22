from matplotlib import pyplot as plt
from spread_test import calculate_spread
from cointegration_test import coint_pairs
from feature_engineering import add_features, backtest
import pandas as pd

while True:
    pairs, df_list = coint_pairs()
    for pair, df in zip(pairs, df_list):
        calculate_spread(df, pair[0], pair[1])
        add_features(df, pair[0], pair[1])
        dfNew=backtest(df)
        dfNew['capital'].plot(title='Pairs Trading Strategy Equity Curve')
        plt.show()