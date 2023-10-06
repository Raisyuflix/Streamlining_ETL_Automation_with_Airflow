import psycopg2 as db
import pandas as pd


def get_data_from_postgresql():
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    df = pd.read_sql(f"select * from table_m3", conn)
    df.to_csv('/opt/airflow/data/P2M3_rais_yufli_data_raw.csv',index=False)

