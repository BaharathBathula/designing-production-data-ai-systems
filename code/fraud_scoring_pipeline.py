# Simple fraud scoring example

transactions = [
    {"customer_id": 101, "amount": 120, "country_risk": 1},
    {"customer_id": 102, "amount": 9500, "country_risk": 3},
    {"customer_id": 103, "amount": 450, "country_risk": 2},
    {"customer_id": 104, "amount": 15000, "country_risk": 5}
]

print("Fraud Scoring Results")
print("---------------------")

for txn in transactions:
    score = (txn["amount"] / 1000) + (txn["country_risk"] * 2)

    if score >= 12:
        decision = "DECLINE"
    elif score >= 6:
        decision = "REVIEW"
    else:
        decision = "APPROVE"

    print(
        f"Customer {txn['customer_id']} | "
        f"Amount ${txn['amount']} | "
        f"Score {round(score,2)} | "
        f"Decision: {decision}"
    )
