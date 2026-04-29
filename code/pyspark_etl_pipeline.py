from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, current_timestamp

# Start Spark session
spark = SparkSession.builder \
    .appName("ProductionETLPipeline") \
    .getOrCreate()

# Read raw CSV data
df = spark.read.option("header", True).csv("input/customers.csv")

# Basic cleansing + transformation
clean_df = df.filter(col("customer_id").isNotNull()) \
    .withColumn("customer_name", upper(col("customer_name"))) \
    .withColumn("processed_timestamp", current_timestamp())

# Write curated output
clean_df.write.mode("overwrite").parquet("output/customers_curated")

print("ETL pipeline completed successfully.")

spark.stop()
