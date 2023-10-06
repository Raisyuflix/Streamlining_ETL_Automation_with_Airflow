import pandas as pd
from elasticsearch import Elasticsearch

def connect_es():
    
    # Koneksi ke Elasticsearch
    es = Elasticsearch(hosts=["http://elasticsearch:9200"])
    df_cleaned = pd.read_csv('/opt/airflow/data/P2M3_rais_yufli_data_clean.csv')

    # Indeksasi data ke Elasticsearch
    for i, r in df_cleaned.iterrows():
        doc = r.to_json()
        res = es.index(index="table_m3", id=i+1, body=doc)
        print(res)