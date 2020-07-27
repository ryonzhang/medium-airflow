from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator



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
    "dummy_operator",
    description="Dummy Operator DAG",
    schedule_interval="0 12 * * *",
    default_args=default_args,
    catchup=False,
)

DummyOperator(task_id="dummy_operator", retries=3, dag=dag)
