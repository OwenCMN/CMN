import streamlit as st
import numpy as np
import joblib

# Load the trained model

model = joblib.load("HA_logistic_regression_model.pkl")

# Title and description

st.title("Heart Attack Prediction App")
st.write(""" This app predicts health risks based on user input. Please provide the following details: 
         """ )

# Input features from the user
age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170, step=1)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70, step=1)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=50, max_value=500, value=200, step=1)
glucose = st.number_input("Glucose (ml/dL)", min_value=50, max_value=500, value=100, step=1)
smoker = st.selectbox("Smoker", ["Yes", "No"])
exercise = st.number_input("Exercise (hours/week)", min_value=0.0, max_value=168.0, value=3.0, step=0.5)
map_value = st.number_input("MAP", min_value=0.0, max_value=300.0, value=90.0, step=0.1)

# Preprocess the inputs
gender_encoded = 1 if gender == "Male" else 0
smoker_encoded = 1 if smoker == "Yes" else 0
inputs = np.array([[age, gender_encoded, height, weight, cholesterol, glucose, smoker_encoded, exercise, map_value]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(inputs)
    risk = "High Risk" if prediction[0] == 1 else "Low Risk"
    st.write(f"Prediction: **{risk}**")

