from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    'bash_operator',
    description="Bash Operator",
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
)


bo1=BashOperator(
    task_id='bash_operator_1',
    bash_command='echo 1',
    dag=dag,
)

bash_command = './bash/bash.sh'

bo2=BashOperator(
    task_id='bash_operator_2',
    bash_command=bash_command,
    dag=dag,
)

bo1>>bo2