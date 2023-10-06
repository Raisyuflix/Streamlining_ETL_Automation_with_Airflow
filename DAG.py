'''
Milestone 3

Nama  : Rais Yufli Xavierullah

Batch : FTDS-HCK-007

Program ini dibuat untuk mengambil data pada database setelah itu akan divisualisasikan dengan menggunakan kibana dan data akan disimpan pada elasticsearh dengan penggunaan airflow 
'''


from airflow.models import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime

from utils.load_data import get_data_from_postgresql
from utils.transform_dataframe import transform_dataframe
from utils.connect_es import connect_es


default_args= {
    'owner': 'Rais',
    'start_date': datetime(2023, 9, 29)
}

with DAG(
    "H8_Automation_Clean",
    description='H8 Automation Clean',
    schedule_interval='@yearly',
    default_args=default_args, 
    catchup=False) as dag:

    # task: 1
    fetching_data = PythonOperator(
        task_id='fetching_data',
        python_callable=get_data_from_postgresql

    )
    
    # task: 2
    cleaning_data = PythonOperator(
        task_id='cleaning_data',
        python_callable=transform_dataframe
    )

    # task: 3
    connect_es = PythonOperator(
        task_id='connect_es',
        python_callable=connect_es
    )


    fetching_data >> cleaning_data >> connect_es