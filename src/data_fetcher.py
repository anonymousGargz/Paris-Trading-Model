# import the necessary packages
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# set the start and end dates for our market data request
end_date = datetime(year=2025, month=6, day=1)
start_date = datetime(year=2023, month=1, day=1)



# define the list of tickers we want to fetch market data for
tickers = ["AAPL", "MSFT"]


def get_ticker_data():
    # download market data for a multiple tickers
    df_multi = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        interval="1d",
        group_by="ticker",
        auto_adjust=True,
        progress=False
    )['Adj Close']
    return df_multi



