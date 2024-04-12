import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load data
fir = pd.read_csv('Datasets/FIR_Details_Data.csv')
accused = pd.read_csv('Datasets/AccusedData (1).csv')
victim = pd.read_csv('Datasets/VictimInfoDetails (1).csv')
fir_short = fir[fir['Year'] == 2023]

def crime_prediction_yearwise(crime_name, crime_data):
    global fir
    crime_type_data = crime_data[crime_data['CrimeHead_Name'] == crime_name]
    crime_counts_per_year = crime_type_data.groupby('Year').size().reset_index(name='Crime_Count')

    X = crime_counts_per_year[['Year']]
    y = crime_counts_per_year['Crime_Count']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Decision Tree Regression Model
    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(X_train, y_train)
    dt_y_pred = dt_model.predict(X_test)
    dt_mae = mean_absolute_error(y_test, dt_y_pred)
    dt_r2 = r2_score(y_test, dt_y_pred)

    # XGBoost Regression Model
    xgb_model = XGBRegressor(random_state=42)
    xgb_model.fit(X_train, y_train)
    xgb_y_pred = xgb_model.predict(X_test)
    xgb_mae = mean_absolute_error(y_test, xgb_y_pred)
    xgb_r2 = r2_score(y_test, xgb_y_pred)

    # st.write(f"Decision Tree Regression MAE: {dt_mae}")
    # st.write(f"Decision Tree Regression R^2 Score: {dt_r2}")
    # st.write(f"XGBoost Regression MAE: {xgb_mae}")
    # st.write(f"XGBoost Regression R^2 Score: {xgb_r2}")

    prediction_method = "Decision Tree Regression" if dt_r2 > xgb_r2 else "XGBoost Regression"
    prediction_model = dt_model if dt_r2 > xgb_r2 else xgb_model
    next_year_prediction = int(prediction_model.predict([[crime_counts_per_year["Year"].max() + 1]])[0])
    st.write(f'Predicted {crime_name} crimes for next year : {next_year_prediction}')

