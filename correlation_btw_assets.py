import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Fetch data
tickers = ["AAPL", "MSFT", "TLT", "NVD", "GLD"]
data = yf.download(tickers, period="1y")['Close']

# 2. Calculate returns
returns = data.pct_change().dropna()

# 3. Correlation matrix
corr_matrix = returns.corr()

# 4. Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1, vmax=1,
    square=True,
    linewidths=0.5,
    annot_kws={"size": 12}
)
plt.title("Stock Correlation Matrix", fontsize=16, pad=20)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()