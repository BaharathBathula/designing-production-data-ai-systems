from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract_data():
    print("Extracting data from source system")


def validate_data():
    print("Validating schema, nulls, and record counts")


def transform_data():
    print("Transforming raw data into curated datasets")


def load_data():
    print("Loading trusted data into analytics layer")


with DAG(
    dag_id="production_data_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["data-engineering", "production"]
) as dag:

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    extract >> validate >> transform >> load
