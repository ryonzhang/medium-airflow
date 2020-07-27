from datetime import datetime

from airflow import DAG,settings
from airflow.models import Connection
from airflow.operators.http_operator import SimpleHttpOperator

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# will add connection every time, so should actually check first if connection is already there
conn = Connection(
        conn_id='http_google',
        conn_type='http',
        host='https://google.de')

session = settings.Session()
session.add(conn)
session.commit()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 22),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

dag = DAG('http_operator', default_args=default_args, schedule_interval='* * * * *') # each minute

SimpleHttpOperator(
    task_id='http_operator',
    log_response=True,
    http_conn_id='http_google',
    method='GET',
    endpoint='',
    dag=dag,
)