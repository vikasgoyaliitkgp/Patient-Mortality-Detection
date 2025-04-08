import streamlit as st
import pickle
import pandas as pd
import joblib
import numpy as np

model = joblib.load('model_weights/et_Gosis_model.pkl')

# Check if the model is of the correct type
if not hasattr(model, 'predict'):
    raise ValueError("Loaded model does not have a 'predict' method. Please check the model file.")
st.title('Patient Mortality Prediction')


# Define the input features in the sidebar with default values
with st.sidebar:
    input_features = {
        'age': st.text_input('Age', '60.318559'),  # Default value for age
        'height': st.text_input('Height (cm)', '169.435677'),  # Default value for height
        'hospital_los_days': st.text_input('Hospital LOS Days', '3.918902'),  # Default value for length of stay in days
        'weight': st.text_input('Weight (kg)', '83.413845'),  # Default value for weight
        'icu_los_days': st.text_input('ICU LOS Days', '0.707497'),  # Default value for ICU length of stay
        'bun_apache': st.text_input('BUN Apache (mg/dL)', '22.585186'),  # Default value for Blood Urea Nitrogen
        'creatinine_apache': st.text_input('Creatinine Apache (mg/dL)', '1.351332'),  # Default value for creatinine levels
        'gcs_eyes_apache': st.text_input('GCS Eyes Apache', '3.664375'),  # Default value for Glasgow Coma Scale Eyes
        'glucose_apache': st.text_input('Glucose Apache (mg/dL)', '155.429448'),  # Default value for blood glucose levels
        'heart_rate_apache': st.text_input('Heart Rate Apache (bpm)', '94.528777'),  # Default value for heart rate
        'hematocrit_apache': st.text_input('Hematocrit Apache (%)', '34.142275'),  # Default value for hematocrit percentage
        'map_apache': st.text_input('MAP Apache (mmHg)', '86.590247'),  # Default value for Mean Arterial Pressure
        'resprate_apache': st.text_input('Respiratory Rate Apache (breaths/min)', '23.782160'),  # Default value for respiratory rate
        'sodium_apache': st.text_input('Sodium Apache (mEq/L)', '138.136288'),  # Default value for sodium levels
        'temp_apache': st.text_input('Temperature Apache (°C)', '36.458278'),  # Default value for body temperature
        'urineoutput_apache': st.text_input('Urine Output Apache (mL)', '1864.964366'),  # Default value for urine output
        'ventilated_apache': st.text_input('Ventilated Apache', '0.187873'),  # Default value for ventilated status
        'wbc_apache': st.text_input('WBC Apache (x10^9/L)', '11.389572'),  # Default value for white blood cell count
        'd1_heartrate_max': st.text_input('D1 Heart Rate Max (bpm)', '98.797676'),  # Default value for max heart rate
        'd1_heartrate_min': st.text_input('D1 Heart Rate Min (bpm)', '68.613108'),  # Default value for min heart rate
        'd1_spo2_max': st.text_input('D1 SpO2 Max (%)', '98.978081'),  # Default value for max oxygen saturation
        'd1_spo2_min': st.text_input('D1 SpO2 Min (%)', '90.534855'),  # Default value for min oxygen saturation
        'd1_sysbp_max': st.text_input('D1 Systolic BP Max (mmHg)', '146.260423'),  # Default value for max systolic blood pressure
        'd1_sysbp_min': st.text_input('D1 Systolic BP Min (mmHg)', '100.518675'),  # Default value for min systolic blood pressure
        'h1_heartrate_max': st.text_input('H1 Heart Rate Max (bpm)', '89.740251'),  # Default value for max heart rate
        'h1_heartrate_min': st.text_input('H1 Heart Rate Min (bpm)', '81.125439'),  # Default value for min heart rate
        'h1_spo2_max': st.text_input('H1 SpO2 Max (%)', '97.952827'),  # Default value for max oxygen saturation
        'h1_spo2_min': st.text_input('H1 SpO2 Min (%)', '95.220407'),  # Default value for min oxygen saturation
        'h1_sysbp_max': st.text_input('H1 Systolic BP Max (mmHg)', '134.198479'),  # Default value for max systolic blood pressure
        'h1_sysbp_min': st.text_input('H1 Systolic BP Min (mmHg)', '118.198281'),  # Default value for min systolic blood pressure
        'd1_potassium_max': st.text_input('D1 Potassium Max (mEq/L)', '4.207813'),  # Default value for max potassium level
        'd1_potassium_min': st.text_input('D1 Potassium Min (mEq/L)', '3.993568')   # Default value for min potassium level
    }

# Create a dataframe from the input features
input_df = pd.DataFrame(input_features, index=[0])

# Convert all inputs to appropriate numeric types
for col in input_df.columns:
    input_df[col] = pd.to_numeric(input_df[col])

# Add title and predict button
if st.button('Predict'):
    # Make predictions using the model
    prediction = model.predict(input_df)
    # Get the probabilities for each class
    probabilities = model.predict_proba(input_df)
    
    # Ensure prediction is a single integer
    predicted_class = int(prediction[0]) if len(prediction) > 0 else None
    
    if predicted_class is not None:
        # Get the probability for the predicted class (0 or 1)
        confidence = probabilities[0][predicted_class]
        
        # Display the prediction and confidence score
        if predicted_class == 0:
            st.markdown(f'Patient is predicted to <font color="green">**survive**</font> in next 24 hours with a confidence score of: **{confidence:.4f}**', unsafe_allow_html=True)
        else:
            st.markdown(f'Patient is predicted to <font color="red" style="font-weight: bold;">**not survive**</font> in next 24 hours with a confidence score of: **{confidence:.4f}**', unsafe_allow_html=True)
    else:
        st.markdown('No prediction could be made.')