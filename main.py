import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_ingestion import DataIngestion

from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig

from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.entity.config_entity import ModelTrainerConfig
#from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_trainer_with_mlflow import ModelTrainer

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate DataIngestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        print(dataingestionartifact)
        logging.info("DataIngestion is successfull.")
        
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, datavalidationconfig)
        logging.info("Initiate DataValidation")
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("DataValidation is successfull.")

        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        data_tranformation = DataTransformation(data_validation_artifact,datatransformationconfig)
        logging.info("Initiate DataTransformation")
        data_transformation_artifact = data_tranformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("DataTransformation is successfull.")

        logging.info("Model Training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model Training artifact created")
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)


#(d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\venv) 
# D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines>python main.py
#DataIngestionArtifact(trained_file_path='Artifacts\\04_07_2025_17_28_15\\data_ingestion\\ingested\\train.csv', test_file_path='Artifacts\\04_07_2025_17_28_15\\data_ingestion\\ingested\\test.csv')
#DataValidationArtifact(validation_status=None, valid_train_file_path='Artifacts\\04_07_2025_17_28_15\\data_ingestion\\ingested\\train.csv', valid_test_file_path='Artifacts\\04_07_2025_17_28_15\\data_ingestion\\ingested\\test.csv', invalid_train_file_path=None, invalid_test_file_path=None, drift_report_file_path='Artifacts\\04_07_2025_17_28_15\\data_validation\\drift_report\\report.yaml')
#DataTransformationArtifact(transformed_object_file_path='Artifacts\\05_07_2025_11_34_51\\data_transformation\\transformed_object\\preprocessing.pkl', transformed_train_file_path='Artifacts\\05_07_2025_11_34_51\\data_transformation\\transformed\\train.npy', transformed_test_file_path='Artifacts\\05_07_2025_11_34_51\\data_transformation\\transformed\\test.npy')