import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
from src.utils import load_object



st.title("""
Flight Fare Prediction
Your Flight Fare Fortune Teller: Plan your trips wisely with our Flight Fare Prediction tool. Compare fares, track trends, and make informed decisions. Never overpay for a ticket again
-- let data guide your travel choices.
""")

st.sidebar.header("User Input Parameter")

# collecting user input feature into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input csv file", type=['csv'])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
            Airline = st.sidebar.selectbox("Airline",('IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 'Multiple carriers', 'GoAir','Vistara', 'Air Asia', 'other'))
            Source = st.sidebar.selectbox("Source",('Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'))
            Destination = st.sidebar.selectbox("Destination",('New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'))
            Total_Stops = st.sidebar.selectbox("Total_Stops",('non-stop', '2 stops', '1 stop', '3 stops'))
            
            journey_day = st.sidebar.slider('journey_day', 1,31)
            journey_month = st.sidebar.slider('journey_month',  1,12)
            Dep_Time_hour = st.sidebar.slider('Dep_Time_hour',1,24 )
            Dep_Time_min = st.sidebar.slider('Dep_Time_min', 1,60)
            Arrival_Time_hour = st.sidebar.slider('Arrival_Time_hour', 1,24)

            Arrival_Time_min = st.sidebar.slider('Arrival_Time_min',1,60)
            Dur_hours = st.sidebar.slider('Dur_hours', 1,24)
            Dur_mins = st.sidebar.slider('Dur_mins', 1,60)

            data = {'Airline': Airline,
                    'Source': Source,
                    'Destination': Destination,
                    'Total_Stops': Total_Stops,
                    'journey_day': journey_day,
                    'journey_month': journey_month,
                    'Dep_Time_hour': Dep_Time_hour,
                    'Dep_Time_min': Dep_Time_min,
                    'Arrival_Time_hour': Arrival_Time_hour,
                    'Arrival_Time_min': Arrival_Time_min,
                    'Dur_hours': Dur_hours,
                    'Dur_mins': Dur_mins
                    }
            features = pd.DataFrame(data, index = [0])
            return features
    input_df =user_input_features()

# combining the input features with entire flight dataset for encoding
raw_data_csv = os.path.join("artifacts","raw_data.csv")
flight_fare = pd.read_csv(raw_data_csv)
df = pd.concat([input_df,flight_fare],axis=0)


# encoding of ordinal features
def prepare_data(df):
    preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
    preprocessor=load_object(file_path=preprocessor_path)
    data_scaled = preprocessor.transform(df)
    return data_scaled


prepared_data = prepare_data(df)

final_df = prepared_data[:1] # Selects only the first row (the user input data)

# Displays the user input features
st.subheader('User Input features')
if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)



# Reading classification model
model_path=os.path.join("artifacts","model.pkl")
model=load_object(model_path)

st.subheader('data')
st.write(input_df)

# making predictions
prediction =  model.predict(final_df)

st.subheader('Flight Fare Prediction')
st.write(prediction)
