import statsmodels.api as sm
import pandas as pd

#CALCULATES SPREAD 
def calculate_spread(df, asset_x, asset_y):
    X = sm.add_constant(df[asset_y])
    model = sm.OLS(df[asset_x], X).fit() # Regression model of asset_x on asset_y
    hedge_ratio = model.params[asset_y] 
    df['spread'] = df[asset_x] - hedge_ratio * df[asset_y] # How different the actual x value is from the expected value
    df['zscore'] = (df['spread'] - df['spread'].rolling(60).mean()) / df['spread'].rolling(60).std() # Standard deviation from the expected line
    return df, hedge_ratio


