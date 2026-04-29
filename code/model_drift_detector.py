import statistics

# Example baseline training predictions
training_scores = [0.10, 0.15, 0.12, 0.18, 0.11]

# Example production predictions
production_scores = [0.30, 0.35, 0.28, 0.33, 0.31]

train_mean = statistics.mean(training_scores)
prod_mean = statistics.mean(production_scores)

drift = abs(prod_mean - train_mean)

print("Model Drift Report")
print("------------------")
print("Training Mean Score:", round(train_mean, 3))
print("Production Mean Score:", round(prod_mean, 3))
print("Drift Magnitude:", round(drift, 3))

if drift > 0.10:
    print("Status: Significant drift detected - retraining recommended")
else:
    print("Status: Stable")
