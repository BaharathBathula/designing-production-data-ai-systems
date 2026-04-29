from kafka import KafkaConsumer
import json

# Connect to Kafka topic
consumer = KafkaConsumer(
    "transactions_topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="fraud-monitor-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for streaming events...")

for message in consumer:
    event = message.value
    print("Received Event:", event)

    # Example business rule
    if event["amount"] > 10000:
        print("ALERT: High-value transaction detected")
