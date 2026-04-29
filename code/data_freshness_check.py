from datetime import datetime, timedelta

# Simulated last data arrival timestamp
last_loaded_time = datetime(2025, 4, 28, 8, 15, 0)

# Freshness SLA (hours)
sla_hours = 2

current_time = datetime.now()
lag = current_time - last_loaded_time

print("Data Freshness Report")
print("---------------------")
print("Last Loaded Time:", last_loaded_time)
print("Current Time:", current_time)
print("Lag:", lag)

if lag > timedelta(hours=sla_hours):
    print("Status: SLA BREACH - Data is stale")
else:
    print("Status: Fresh and within SLA")
