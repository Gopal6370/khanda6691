import pandas as pd

df = pd.read_csv("ecommerce_data.csv")

print(df.head())

print("\nDataset Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())