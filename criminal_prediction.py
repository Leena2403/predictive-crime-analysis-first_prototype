import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
fir_data = pd.read_csv('Datasets/FIR_Details_Data.csv')

def train_and_predict_fir_crime_model(fir_data, firid, unitid, crimeno):

    X = fir_data[['FIR_ID', 'Unit_ID','Crime_No']]
    y = fir_data['CrimeHead_Name']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X['FIR_ID'] = X['FIR_ID'].astype(int)

    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    new_input = {'FIR_ID':firid,'Unit_ID':unitid,'Crime_No':crimeno}
    new_prediction = classifier.predict(pd.DataFrame([new_input]))
    predicted_crime_head = new_prediction[0]
    st.write(f'Predicted CrimeHead_Name: {predicted_crime_head}')
    # st.write(f'Accuracy Score: {accuracy}')