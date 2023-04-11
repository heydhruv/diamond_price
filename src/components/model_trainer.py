import os
import sys
import numpy as np
from src.exception import CustomException 
from src.logger import logging 
import pandas as pd
from dataclasses import dataclass
from src.utils import evaluate_model

from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from src.utils import save_obj


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('splitting dependent and independent features from train & test data')

            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
        
            models={"LinearRegression":LinearRegression(),'Lasso':Lasso(),'Ridge':Ridge(),'ElasticNet':ElasticNet()}

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print('\n=================================================')
            print(model_report)
            print('\n=================================================')
            logging.info(f'model report: {model_report}')

            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]

            print(f"best model found model name:{best_model_name},r2_score: {best_model_score}")
            print('\n=====================================================')
            logging.info(f'best model found {best_model_name},r2_score: {best_model_score}')

            save_obj(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)
        except Exception as e:
            logging.info('exception occured at model training')
            raise CustomException(e,sys)
