import streamlit as st
import pickle
import pandas as pd
import joblib


model = joblib.load('model_weights/et_Gosis_model.pkl')

# Check if the model is of the correct type
if not hasattr(model, 'predict'):
    raise ValueError("Loaded model does not have a 'predict' method. Please check the model file.")
st.title('Patient Mortality Prediction')
# ... existing code ...

# Define the input features in the sidebar
with st.sidebar:
   input_features = {
    'age': st.slider('Age', 1, 150),  # Typical human age range
    'height': st.slider('Height (cm)', 50, 250),  # Height in centimeters
    'hospital_los_days': st.slider('Hospital LOS Days', 0, 365),  # Length of stay in days
    'weight': st.slider('Weight (kg)', 2, 300),  # Weight in kilograms
    'icu_los_days': st.slider('ICU LOS Days', 0, 100),  # ICU length of stay in days
    'bun_apache': st.slider('BUN Apache (mg/dL)', 2, 150),  # Blood Urea Nitrogen
    'creatinine_apache': st.slider('Creatinine Apache (mg/dL)', 0.1, 15.0),  # Creatinine levels
    'gcs_eyes_apache': st.slider('GCS Eyes Apache', 1, 4),  # Glasgow Coma Scale Eyes
    'glucose_apache': st.slider('Glucose Apache (mg/dL)', 40, 600),  # Blood glucose levels
    'heart_rate_apache': st.slider('Heart Rate Apache (bpm)', 30, 200),  # Heart rate in beats per minute
    'hematocrit_apache': st.slider('Hematocrit Apache (%)', 10, 60),  # Hematocrit percentage
    'map_apache': st.slider('MAP Apache (mmHg)', 30, 150),  # Mean Arterial Pressure
    'resprate_apache': st.slider('Respiratory Rate Apache (breaths/min)', 5, 60),  # Respiratory rate
    'sodium_apache': st.slider('Sodium Apache (mEq/L)', 120, 160),  # Sodium levels
    'temp_apache': st.slider('Temperature Apache (°C)', 25, 45),  # Body temperature in Celsius
    'urineoutput_apache': st.slider('Urine Output Apache (mL)', 0, 10000),  # Urine output in mL
    'ventilated_apache': st.slider('Ventilated Apache', 0, 1),  # Binary: 0 for no, 1 for yes
    'wbc_apache': st.slider('WBC Apache (x10^9/L)', 0.1, 100.0),  # White blood cell count
    'd1_heartrate_max': st.slider('D1 Heart Rate Max (bpm)', 30, 220),  # Max heart rate
    'd1_heartrate_min': st.slider('D1 Heart Rate Min (bpm)', 30, 220),  # Min heart rate
    'd1_spo2_max': st.slider('D1 SpO2 Max (%)', 70, 100),  # Max oxygen saturation
    'd1_spo2_min': st.slider('D1 SpO2 Min (%)', 70, 100),  # Min oxygen saturation
    'd1_sysbp_max': st.slider('D1 Systolic BP Max (mmHg)', 50, 250),  # Max systolic blood pressure
    'd1_sysbp_min': st.slider('D1 Systolic BP Min (mmHg)', 50, 250),  # Min systolic blood pressure
    'h1_heartrate_max': st.slider('H1 Heart Rate Max (bpm)', 30, 220),  # Max heart rate
    'h1_heartrate_min': st.slider('H1 Heart Rate Min (bpm)', 30, 220),  # Min heart rate
    'h1_spo2_max': st.slider('H1 SpO2 Max (%)', 70, 100),  # Max oxygen saturation
    'h1_spo2_min': st.slider('H1 SpO2 Min (%)', 70, 100),  # Min oxygen saturation
    'h1_sysbp_max': st.slider('H1 Systolic BP Max (mmHg)', 50, 250),  # Max systolic blood pressure
    'h1_sysbp_min': st.slider('H1 Systolic BP Min (mmHg)', 50, 250),  # Min systolic blood pressure
    'd1_potassium_max': st.slider('D1 Potassium Max (mEq/L)', 2.5, 7.0),  # Max potassium level
    'd1_potassium_min': st.slider('D1 Potassium Min (mEq/L)', 2.5, 7.0)   # Min potassium level
}

# Create a dataframe from the input features
input_df = pd.DataFrame(input_features, index=[0])

# Add title and predict button
if st.button('Predict'):
    # Make predictions using the model
    prediction = model.predict(input_df)
    # Display the prediction
    st.write('Prediction:', prediction)

