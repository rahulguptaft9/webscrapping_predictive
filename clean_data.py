import pandas as pd

df = pd.read_csv("scraped_data.csv")
print(df.columns.tolist())
# No need to create stock_binary again, it's already in the CSV
# Just make sure price is clean
df['price_gbp'] = df['price_gbp'].fillna(df['price_gbp'].median())

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("Cleaned data written to cleaned_data.csv")