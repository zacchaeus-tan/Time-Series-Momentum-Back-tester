import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "TLT", "NVD", "GLD"]
data = yf.download(tickers, period="2y")['Close']

#log returns
for stock in data.columns:
    log_returns = np.log(data[stock] / data[stock].shift(1))

#rolling mean and std
    WINDOW_SIZE = 20
# for stock in data.columns:
    rolling_mean = log_returns.rolling(window=WINDOW_SIZE,min_periods=WINDOW_SIZE).mean()
    rolling_std = log_returns.rolling(window=WINDOW_SIZE,min_periods=WINDOW_SIZE).std(ddof=1) #ddof uses the sample std (divide by n-1)

# for stock in data.columns:
    print(f"Mean daily log return for {stock} : {log_returns.mean():.5f}  ({log_returns.mean()*100:.3f}%)")
    print(f"Std  daily log return for {stock} : {log_returns.std():.5f}  ({log_returns.std()*100:.3f}%)")
    print(f"Annualised return     for {stock} : {log_returns.mean() * 252:.4f}  ({log_returns.mean()*252*100:.1f}%)")
    print(f"Annualised volatility for {stock} : {log_returns.std() * np.sqrt(252):.4f}  ({log_returns.std()*np.sqrt(252)*100:.1f}%)")
    # 252 = trading days in a year