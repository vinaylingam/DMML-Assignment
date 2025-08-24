from prefect import flow, task
import papermill as pm
from data_ingestion.data_Ingestion_code import fetchData
from data_validation.data_validation_code import validateData
from data_preparation.data_process import data_prepare

@task
def data_ingestion():
    fetchData()
    print("Data Ingestion completed")

@task
def data_validation():
    validateData()
    print("Data validation completed")

@task
def data_preparation():
    data_prepare()
    print("data preparation completed")
    pass

@task
def data_transformation():
    print("data transformation completed")
    pass

@task
def feature_store():
    print("data features stored in sqlite database")
    pass

@task
def train_model():
    print("model is trained and it's version is stored")
    pass

@flow
def churn_pipeline():
    #data_ingestion()
    data_validation()  
    data_preparation()  

if __name__ == "__main__":
    churn_pipeline()