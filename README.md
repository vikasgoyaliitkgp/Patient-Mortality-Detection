# Project Overview

This project is a Streamlit application designed to predict patient mortality based on various medical parameters. The application utilizes a pre-trained machine learning model to make predictions based on user input.

# Features

The application includes the following features:

1. **User Input**: Users can input various medical parameters such as age, height, weight, hospital length of stay, ICU length of stay, and several Apache II score parameters.
2. **Model Prediction**: The application uses a pre-trained machine learning model to predict patient mortality based on the input parameters.
3. **Prediction Display**: The prediction is displayed to the user, indicating the likelihood of patient mortality.

# Technical Details

1. **Model**: The model used for prediction is a pre-trained model stored in the 'model_weights' directory. The model is loaded using joblib.
2. **Streamlit**: The application is built using Streamlit, a Python library for creating web applications for machine learning and data science.
3. **Pandas**: The application uses Pandas for data manipulation and creation of a dataframe from user input.
4. **Joblib**: Joblib is used for loading the pre-trained model.

# How to Use

1. **Launch the Application**: Run the application by executing the 'streamlit_app.py' file.
2. **Input Parameters**: In the sidebar, input the required medical parameters.
3. **Predict**: Click the 'Predict' button to make a prediction based on the input parameters.
4. **View Prediction**: The prediction will be displayed on the main page.

# Executing the Code

To execute the code, follow these steps:

1. **Install Required Libraries**: Install the required libraries by running `pip install streamlit pandas joblib` in your terminal.
2. **Download the Model**: Download the pre-trained model from the 'model_weights' directory.
3. **Run the Application**: Run the application by executing `streamlit run streamlit_app.py` in your terminal.
4. **Access the Application**: Access the application by navigating to `http://localhost:8501` in your web browser.

# Future Development

This project is open to future development and improvement. Some potential areas for expansion include:

1. **Model Improvement**: Refining the machine learning model to improve prediction accuracy.
2. **Additional Parameters**: Incorporating more medical parameters to increase the accuracy of predictions.
3. **User Interface Enhancements**: Enhancing the user interface to make it more user-friendly and intuitive.

# Contributing

Contributions to this project are welcome. If you have any suggestions or improvements, please feel free to submit a pull request.

