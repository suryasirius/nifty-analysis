import pandas as pd

df = pd.read_csv("nifty.csv")
print(df.head())

print("Rows and columns:", df.shape)
print("First date:", df["Date"].min())
print("Last date:", df["Date"].max())
print(df.describe())