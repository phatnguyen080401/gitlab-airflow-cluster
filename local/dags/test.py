from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a Python function for the PythonOperator
def print_hello():
    print("Hello from PythonOperator!")

def print_goodbye():
    print("Goodbye from PythonOperator!")

with DAG(
    dag_id='simple_test_dag',
    start_date=datetime(2025,6,1),
    schedule=None, 
    catchup=False,         
    tags=['example', 'testing'], 
) as dag:
    start_task = BashOperator(
        task_id='start_greeting',
        bash_command='echo "Starting the simple test DAG!"',
    )

    hello_task = PythonOperator(
        task_id='print_hello_message',
        python_callable=print_hello,
    )

    sleep_task = BashOperator(
        task_id='wait_a_bit',
        bash_command='echo "Sleeping for 5 seconds..." && sleep 5',
    )

    goodbye_task = PythonOperator(
        task_id='print_goodbye_message',
        python_callable=print_goodbye,
    )

    end_task = BashOperator(
        task_id='end_greeting',
        bash_command='echo "Simple test DAG completed!"',
    )

    start_task >> hello_task >> sleep_task >> goodbye_task >> end_task