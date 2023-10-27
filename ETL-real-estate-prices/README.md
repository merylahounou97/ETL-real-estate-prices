# Real Estate Prices ETL

[![Generic badge](https://img.shields.io/badge/Apache_Airflow-2.2.2-blue.svg)](https://airflow.apache.org/)
[![Generic badge](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/PySpark-3.1.2-blue.svg)](https://spark.apache.org/docs/latest/api/python/#)
[![Generic badge](https://img.shields.io/badge/Delta-1.0.0-blue.svg)](https://delta.io/)
[![Generic badge](https://img.shields.io/badge/Jupyter_Notebook-6.4.12-blue.svg)](https://jupyter.org/)
[![Generic badge](https://img.shields.io/badge/Papermill-2.3.4-blue.svg)](https://papermill.readthedocs.io/en/latest/)
[![Generic badge](https://img.shields.io/badge/Apache_Druid-0.23.0-blue.svg)](https://druid.apache.org/)
[![Generic badge](https://img.shields.io/badge/Apache_Superset-1.5.0-blue.svg)](https://superset.apache.org/)
[![Generic badge](https://img.shields.io/badge/Docker-20.10.6-blue.svg)](https://www.docker.com/)

The following project is based on [Building a Data Engineering Project in 20 Minutes](https://www.sspaeti.com/blog/data-engineering-project-in-twenty-minutes/), where the idea is to:
- build a scrapper to real estate data
- process the scrapped data using `PySpark` inside `Jupyter Notebooks`
- store the processed data on `delta` tables
- build a ML to predict the house prices
- ingest the predicted data to `Apache Druid`
- connect `Apache Superset` to the `Apache Druid` DB, and create a dashboard to keep track of the ML model performance
- orchestrate everything using `Apache Airflow` running inside `docker` containers

So, in summary, we want to build an ETL scrapping the prices and data from a web site, process that retrieved data to build a ML model, and create a dashboard to inspect the model performance.
