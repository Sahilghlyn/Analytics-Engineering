import pandas as pd
import os

# Paths
input_file = os.path.join("..", "data", "orders.csv")
output_file = os.path.join("..", "data", "aggregated_sales.csv")

# Load CSV
df = pd.read_csv(input_file, parse_dates=['order_date'])

# Add total sales column
df['total_sales'] = df['quantity'] * df['price']

# Aggregate: total sales per month
df_monthly = df.groupby(df['order_date'].dt.to_period('M')).total_sales.sum().reset_index()
df_monthly['order_date'] = df_monthly['order_date'].dt.to_timestamp()

# Aggregate: top 5 products by revenue
df_products = df.groupby('product').total_sales.sum().reset_index()
df_products = df_products.sort_values(by='total_sales', ascending=False).head(5)

# Save aggregated data
df_monthly.to_csv(os.path.join("..", "data", "monthly_sales.csv"), index=False)
df_products.to_csv(os.path.join("..", "data", "top_products.csv"), index=False)

print("ETL completed. Aggregated CSVs saved in data/")
