import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os
class PredictPipline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            return CustomException(e, sys)
    
class CustomData:
    def __init__(self,
        Airline : str,
        Source : str,
        Destination : str,
        Total_Stops : str,
        journey_day:int,
        journey_month:int,	
        Dep_Time_hour:int,
        Dep_Time_min:int,	
        Arrival_Time_hour:int,
        Arrival_Time_min : int,	
        Dur_hours : int, 
        Dur_mins: int):

        self.Airline = Airline

        self.Source = Source

        self.Destination = Destination

        self.Total_Stops = Total_Stops

        self.journey_day = journey_day

        self.journey_month = journey_month

        self.Dep_Time_hour = Dep_Time_hour

        self.Dep_Time_min = Dep_Time_min
        
        self.Arrival_Time_hour = Arrival_Time_hour
        
        self.Arrival_Time_min = Arrival_Time_min 
        
        self.Dur_hours = Dur_hours 

        self.Dur_mins = Dur_mins 
        
    def get_data_as_data_frame(self):
        try:
             custom_data_input_dict = {
                "Airline": [self.Airline],
                "Source": [self.Source],
                "Destination": [self.Destination],
                "Total_Stops": [self.Total_Stops],
                "journey_day": [self.journey_day],
                "journey_month": [self.journey_month],
                "Dep_Time_hour": [self.Dep_Time_hour],
                "Dep_Time_min": [self.Dep_Time_min],
                "Arrival_Time_hour": [self.Arrival_Time_hour],
                "Arrival_Time_min": [self.Arrival_Time_min],
                "Dur_hours": [self.Dur_hours],
                "Dur_mins": [self.Dur_mins],
            }
             
             return pd.DataFrame(custom_data_input_dict)
       
        except Exception as e:
            return CustomException(e,sys)