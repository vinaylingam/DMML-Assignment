from prefect import flow, task
import papermill as pm
from data_ingestion.data_Ingestion_code import fetchData
from data_validation.data_validation_code import validateData
from data_preparation.data_process import data_prepare
from feature_store.feature_store_code import saveData

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

@task
def data_transformation():
    pm.execute_notebook(
        "data_transformation/data_transformation_code.ipynb",   # input notebook
        "data_transformation/data_transformation_code_output.ipynb",  # output notebook with executed cells
    )
    print("data transformation completed")

@task
def feature_store():
    saveData()
    print("data features stored in sqlite database")
    pass

@task
def train_model():
    pm.execute_notebook(
        "model_building/NeuralNetwork.ipynb",   # input notebook
        "model_building/NeuralNetwork_Output.ipynb",  # output notebook with executed cells
    )
    print("model is trained and it's version is stored")
    pass

@flow
def churn_pipeline():
    #data_ingestion()
    #data_validation()  
    #data_preparation()  
    data_transformation()
    feature_store()
    train_model()

if __name__ == "__main__":
    churn_pipeline()