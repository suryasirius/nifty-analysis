import yfinance as yf

data = yf.download("^NSEI", start="2023-01-01", end="2025-12-31")
data.columns = data.columns.get_level_values(0)
print(data.head())
data.to_csv("nifty.csv")