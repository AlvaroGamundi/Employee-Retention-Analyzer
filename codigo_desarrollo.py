import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

def ejecutar_modelos(temp):
    
    
        #6.CARGA PIPES DE EJECUCION
        with open('pipe_ejecucion.pickle', mode='rb') as file:
           pipe_ejecucion= pickle.load(file)
    
        
    
    
        #7.EJECUCION
        scoring = pipe_ejecucion.predict_proba(temp)[:, 1]
        
    
    
        #8.RESULTADO
        Probabilidad_abandono=np.round(scoring * 100, 1)


        return(Probabilidad_abandono)