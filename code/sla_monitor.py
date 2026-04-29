# Simulated pipeline SLA metrics

pipelines = [
    {"name": "customer_daily_load", "target_minutes": 30, "actual_minutes": 28},
    {"name": "sales_hourly_refresh", "target_minutes": 15, "actual_minutes": 18},
    {"name": "fraud_stream_batch_sync", "target_minutes": 10, "actual_minutes": 9},
]

print("Pipeline SLA Dashboard")
print("----------------------")

for pipeline in pipelines:
    name = pipeline["name"]
    target = pipeline["target_minutes"]
    actual = pipeline["actual_minutes"]

    if actual <= target:
        status = "PASS"
    else:
        status = "BREACH"

    print(f"{name} | Target: {target} min | Actual: {actual} min | Status: {status}")
