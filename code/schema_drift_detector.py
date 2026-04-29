import json

# Expected schema definition
expected_schema = {
    "customer_id": "int",
    "customer_name": "string",
    "email": "string",
    "country": "string"
}

# Incoming schema from source system
incoming_schema = {
    "customer_id": "int",
    "customer_name": "string",
    "email_address": "string",
    "country": "string"
}

missing_columns = []
new_columns = []
type_changes = []

# Detect missing / changed columns
for column, dtype in expected_schema.items():
    if column not in incoming_schema:
        missing_columns.append(column)
    elif incoming_schema[column] != dtype:
        type_changes.append((column, dtype, incoming_schema[column]))

# Detect new columns
for column in incoming_schema:
    if column not in expected_schema:
        new_columns.append(column)

print("Schema Drift Report")
print("-------------------")
print("Missing Columns:", missing_columns)
print("New Columns:", new_columns)
print("Type Changes:", type_changes)

if missing_columns or new_columns or type_changes:
    print("Status: DRIFT DETECTED")
else:
    print("Status: SCHEMA OK")
