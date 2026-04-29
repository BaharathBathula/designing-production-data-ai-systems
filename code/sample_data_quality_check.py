import pandas as pd

# Sample dataset
data = {
    "customer_id": [1, 2, 3, None],
    "email": ["a@test.com", "b@test.com", None, "d@test.com"],
    "amount": [100, 250, -50, 300]
}

df = pd.DataFrame(data)

# Basic checks
null_customer_ids = df["customer_id"].isnull().sum()
null_emails = df["email"].isnull().sum()
negative_amounts = (df["amount"] < 0).sum()

print("Data Quality Report")
print("-------------------")
print(f"Missing customer_id: {null_customer_ids}")
print(f"Missing email: {null_emails}")
print(f"Negative amounts: {negative_amounts}")

if null_customer_ids == 0 and null_emails == 0 and negative_amounts == 0:
    print("Status: PASS")
else:
    print("Status: FAIL")
