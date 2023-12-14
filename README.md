# Streamlining ETL Automation with Airflow
---

## Introduction
---
This project focuses on streamlining ETL (Extract, Transform, Load) automation using Apache Airflow. The ETL process is designed to automate the transformation and loading of data from a PostgreSQL database to Elasticsearch.
## Data Source
---
The dataset used in this project from kaggle [link](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction) , which contains 13 features.
## Technologies and Libraries Used
---
- Python
- Apache Airflow
- pandas
- PostgreSQL
- Elasticsearch

## ETL Automation Workflow
---
`DAG.py` defines the DAG, and Apache Airflow is used to coordinate the ETL process.

## Data Transformation
---
The pandas package is used to facilitate the execution of data transformations in Python, as described in `transform_dataframe.py.`

## Data Loading
---
Elasticsearch is used to load the modified data for additional analysis and visualization.
