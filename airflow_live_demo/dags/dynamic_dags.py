from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta
import requests
import random

# Fetch Simulator instances from Django
def fetch_simulator_instances():
    response = requests.get('http://172.22.0.1:8000/api/simulators/')
    return response.json()

# Task to call the KPI endpoint
def call_kpi_endpoint(value, kpi_id):
    response = requests.post(
        'http://172.22.0.1:8000/api/kpis/kpi/',
        json={'value': value, 'kpi_id': kpi_id}
    )
    print(response.json())

# Dynamically create DAGs
simulators = fetch_simulator_instances()
for simulator in simulators:
    dag_id = f"simulator_{simulator['id']}"
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime.strptime(simulator['start_date'], '%Y-%m-%dT%H:%M:%S'),
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }

    with DAG(
        dag_id,
        default_args=default_args,
        schedule_interval=simulator['interval'],
        catchup=False,
    ) as dag:

        random_value = random.randint(1, 100)
        task = PythonOperator(
            task_id='generate_random_value',
            python_callable=lambda: call_kpi_endpoint(random_value, simulator['kpi_id'])
        )
