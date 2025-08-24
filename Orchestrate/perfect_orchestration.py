from prefect import flow, task
import papermill as pm
from data_ingestion.data_Ingestion_code import fetchData

@task
def data_ingestion():
    fetchData()
    print("Data Ingestion completed")

@flow
def churn_pipeline():
    data_ingestion()    

if __name__ == "__main__":
    churn_pipeline()