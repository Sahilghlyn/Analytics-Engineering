import pandas as pd

# Load raw data
df = pd.read_csv('../data/orders.csv')

# Simple cleaning
df = df.drop_duplicates()
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Aggregation example
sales_summary = df.groupby('ProductID')['Quantity'].sum().reset_index()

# Save processed file
sales_summary.to_csv('../data/sales_summary.csv', index=False)

print("ETL pipeline completed successfully!")
