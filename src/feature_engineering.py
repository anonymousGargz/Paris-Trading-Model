import statsmodels.api as sm
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def add_features(df, asset_x, asset_y):
    # Calculate 5-day forward returns from the spread
    df['future_return'] = df['spread'].shift(-5) - df['spread']

    # Create binary label: was this trade profitable?
    df['label'] = (df['future_return'] > 0).astype(int)

    # Add more features:
    df['zscore_lag1'] = df['zscore'].shift(1) 
    df['zscore_diff'] = df['zscore'] - df['zscore_lag1'] #Check if zscore is still increasing - possible premature trade
    df['volatility'] = df['spread'].rolling(20).std() #Market volatility and noise
    df['price_ratio'] = df[asset_x] / df[asset_y] #Check mispricing
    
    features = ['zscore', 'zscore_lag1', 'zscore_diff', 'volatility', 'price_ratio']
    X = df[features].dropna()
    y = df['label'].loc[X.index]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Excellent for classification problems
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # ...existing code...

    # Align predictions with the correct indices
    df.loc[X.index, 'ml_pred'] = model.predict(X)

    # Initialize signal column
    df['signal'] = None

    # Assign signals based on conditions
    df.loc[(df['ml_pred'] == 1) & (df['zscore'] > 1.0), 'signal'] = 'SHORT'
    df.loc[(df['ml_pred'] == 1) & (df['zscore'] < -1.0), 'signal'] = 'LONG'
    df.loc[abs(df['zscore']) < 0.2, 'signal'] = 'EXIT'

    print(df.iloc[0:251][df['signal'].isin(['SHORT', 'LONG'])])
# ...existing code...



def backtest(df):
    capital = 100000
    position = 0
    capital_curve = []

    for i in range(1, len(df)):
        signal = df.iloc[i]['signal']
        prev_spread = df.iloc[i - 1]['spread']
        spread = df.iloc[i]['spread']

        if signal == 'LONG':
            position = +1
        elif signal == 'SHORT':
            position = -1
        elif signal == 'EXIT':
            position = 0

        pnl = position * (spread - prev_spread)
        capital += pnl
        capital_curve.append(capital)
    df['capital']=None
    df = df.iloc[1:].copy()
    df['capital'] = capital_curve
    return df



