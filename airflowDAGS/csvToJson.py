"""
Building a CSV to a JSON data pipeline
Starting with a simple DAG will help you understand how Airflow works and will help you to add more 
functions to build a better data pipeline. The DAG you build will print out a message using Bash, 
then read the CSV and print a list of all the names. The following steps will walk you through building 
the data pipeline:
"""
import pandas as pd
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def csvToJson():
    df = pd.read_csv(
        '/goinfre/sbahaddi/gits/DataEngineering_Infrastructure/data/faker_data.csv')
    for _, r in df.iterrows():
        print(r['name'])
    df.to_json('dags/fromAirflow.json', orient='records')


default_args = {
    'owner': 'sbahaddi',
    'start_date': dt.datetime(2021, 3, 26),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),
         # '0 * * * *',
         ) as dag:
    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "I am reading the CSV now....."')
    convertTojSON = PythonOperator(task_id='convertCSVtoJson',
                                   python_callable=csvToJson)
    print_starting >> convertTojSON
