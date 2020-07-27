from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_hello():
    return "Hello world!"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 1, 1),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

dag = DAG(
    "python_operator",
    description="Python Operator",
    schedule_interval="0 12 * * *",
    default_args=default_args,
    catchup=False,
)

PythonOperator(task_id="python_operator", python_callable=print_hello, dag=dag)

