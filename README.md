# Airflow Simulation Project

This repository contains the code for the Apache Airflow simulation project. The goal of the project is to demonstrate the capabilities of Apache Airflow in managing workflows and data pipelines.

## Project Overview

This project integrates Django and Apache Airflow to dynamically generate DAGs based on a Simulator model. Each DAG schedules tasks to generate random values, call a KPI endpoint, and process the response.

## Setup Steps
### 1. Airflow Setup

1. Download and set up Airflow using Docker.

2. Create dags, logs, and plugins folders.

3. Use docker-compose.yaml to start Airflow.

4. Access the Airflow UI at http://localhost:8080.

### 2. Django Setup

1. Create a Django project with simulator and kpis apps.

2. Add the Simulator model and the KPI endpoint.

3. Run migrations and start the Django server.

4. Test endpoints using Postman.

## Dynamic DAGs

- Dynamic DAGs are created in dynamic_dags.py based on Simulator model instances.

- DAGs fetch random values and call the KPI endpoint.

## Testing Steps
### Django
1. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Open the admin interface at http://127.0.0.1:8000/admin and add Simulator instances.

3. Test the KPI endpoint using Postman:
   - URL: http://127.0.0.1:8000/api/kpis/kpi/
   - Method: POST
   - Body (JSON):
   ```bash
   {
    "value": 100,
    "kpi_id": 1
    }
   ```
  - Expected Response:
    ```bash
     {
    "input_value": 100,
    "kpi_id": 1,
    "result": 600.0
    }
    ```
### Airflow
1. Start Airflow using Docker:
   ```bash
     docker-compose up airflow-init
     docker-compose up
    ```
3. Access the Airflow UI at http://localhost:8080.
4. Verify the dynamically created DAGs for each Simulator instance.
5. Trigger a DAG manually and monitor the task execution.
6. Check the logs in the Airflow UI to ensure tasks are executed successfully.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hebaraslan2001/airflow_simulation.git
    ```

2. Install the required dependencies:

    ```bash
    cd airflow_simulation
    pip install -r requirements.txt
    ```

