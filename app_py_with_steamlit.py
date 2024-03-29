# -*- coding: utf-8 -*-
"""app_py_with_Steamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iaZKXWC_4kTBQjis5ZvKZkhCBzhOZT5m

**Create app.py file**
"""

!pip install streamlit
import streamlit as st
import pickle
import numpy as np

# Load the model
model_name = open('/content/final_log_reg_model.pkl', 'rb')
svm_model = pickle.load(model_name)

def predict(gender, ssc_p, hsc_p, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p):
    # Convert categorical inputs to numerical values
    gender = 0 if gender == 'M' else 1
    degree_t1 = {'Sci&Tech': 2, 'Comm&Mgmt': 0, 'Others': 1}.get(degree_t)
    workex1 = 1 if workex == 'Yes' else 0
    hsc_s1 = {'Commerce': 1, 'Science': 2, 'Arts': 0}.get(hsc_s)
    specialisation1 = 1 if specialisation == 'Mkt&HR' else 0

    # Make predictions
    pred_args = np.array([gender, ssc_p, hsc_p, hsc_s1, degree_p, degree_t1, workex1, etest_p, specialisation1, mba_p]).reshape(1,-1)
    y_pred = svm_model.predict(pred_args)[0]
    return y_pred

def main():
    st.title('Campus Placement Prediction')

    # Add UI components for user inputs
    gender = st.radio('Gender', ('Male', 'Female'))
    ssc_p = st.number_input('SSC Percentage', min_value=0.0, max_value=100.0, step=0.1)
    hsc_p = st.number_input('HSC Percentage', min_value=0.0, max_value=100.0, step=0.1)
    hsc_s = st.selectbox('HSC Stream', ('Commerce', 'Science', 'Arts'))
    degree_p = st.number_input('Degree Percentage', min_value=0.0, max_value=100.0, step=0.1)
    degree_t = st.selectbox('Degree Type', ('Sci&Tech', 'Comm&Mgmt', 'Others'))
    workex = st.radio('Work Experience', ('Yes', 'No'))
    etest_p = st.number_input('E-Test Percentage', min_value=0.0, max_value=100.0, step=0.1)
    specialisation = st.selectbox('MBA Specialisation', ('Mkt&HR', 'Mkt&Fin'))
    mba_p = st.number_input('MBA Percentage', min_value=0.0, max_value=100.0, step=0.1)

    # Make prediction when the button is clicked
    if st.button('Predict'):
        result = predict(gender, ssc_p, hsc_p, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p)
        if result == 0:
            st.write("Work Hard!!! Chances are less")
        else:
            st.write("You are Doing well!! You Will Get placements")

if __name__ == '__main__':
    main()

