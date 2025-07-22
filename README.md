# 📈 Statistical Arbitrage & Pairs Trading with Machine Learning

This project implements a **machine learning-enhanced statistical arbitrage strategy** using **pairs trading**. It identifies cointegrated asset pairs (e.g., AAPL/MSFT), generates trading signals based on the spread's z-score, and uses a supervised ML model to filter high-confidence opportunities.

---

## 🚀 Project Features

- ✅ Cointegration test to select valid trading pairs
- 📊 Spread modeling using linear regression (hedge ratio)
- 📉 Z-score based signal generation (long, short, exit)
- 🤖 Machine learning model (XGBoost) to predict profitable trades
- 📈 Backtesting framework to simulate strategy performance
- 🔮 Live prediction pipeline for real-time signal generation

---

## 📂 Project Structure (Some files not added yet)

pairs_trading_project/
├── data/ # Historical price data (optional cache)
├── notebooks/ # EDA and model development
├── src/
│ ├── data_loader.py # Fetch historical data
│ ├── cointegration.py # Cointegration tests
│ ├── spread_model.py # Calculate spread & z-score
│ ├── signal_generator.py # Generate trade signals
│ ├── ml_model.py # Train & evaluate ML classifier
│ ├── backtest.py # Simulate strategy
├── main.py # Run full pipeline
├── predict_live.py # Make predictions on current market data
├── requirements.txt # Python dependencies
└── README.md
