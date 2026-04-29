# Simulated access log records

access_logs = [
    {"user": "analyst_01", "dataset": "sales_curated", "approved": True},
    {"user": "intern_02", "dataset": "customer_pii", "approved": False},
    {"user": "engineer_03", "dataset": "fraud_features", "approved": True},
    {"user": "vendor_04", "dataset": "claims_phi", "approved": False}
]

print("Access Governance Audit")
print("-----------------------")

violations = 0

for record in access_logs:
    if not record["approved"]:
        violations += 1
        print(
            f"UNAUTHORIZED ACCESS ATTEMPT | User: {record['user']} | Dataset: {record['dataset']}"
        )

print("-----------------------")
print("Total Violations:", violations)
