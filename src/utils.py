import os,sys
import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from src.exception import CustomException
from src.logger import logging

def save_obj(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)        