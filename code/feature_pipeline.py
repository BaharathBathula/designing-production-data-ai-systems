import pandas as pd

# Sample customer transactions
data = {
    "customer_id": [101, 101, 102, 103, 103],
    "transaction_amount": [120, 80, 250, 40, 60]
}

df = pd.DataFrame(data)

# Build ML features
features = df.groupby("customer_id").agg(
    total_spend=("transaction_amount", "sum"),
    avg_spend=("transaction_amount", "mean"),
    txn_count=("transaction_amount", "count")
).reset_index()

print("Feature Pipeline Output")
print("-----------------------")
print(features)
