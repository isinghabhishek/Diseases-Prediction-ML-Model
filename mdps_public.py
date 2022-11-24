# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:31:27 2022

@author: ABHISHEK SINGH
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved Model
diabetes_model = pickle.load(open('diabetic_model.sav', 'rb'))
hearts_model = pickle.load(open('heart_disease_model.sav', 'rb'))


# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                           
                           ['Diabetic Prediction',
                            'Heart Disease Prediction System'],
                           
                           icons=['activity', 'heart'],
                           
                           default_index = 0)
    
# Diabetes Prediction Page
if(selected == 'Diabetic Prediction'):
    
    # page title
    st.title('Diabetic Prediction Using ML')
    
    # getting the input data from the user
    #column for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnacies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThikness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThikness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_diagnosis[0] == 1):
            diab_diagnosis = 'The Person Is Diabetic'
            
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
            
    st.success(diab_diagnosis)
    
    
    
    
# Heart disease Prediction Page

if(selected == 'Heart Disease Prediction System'):
    
    # page title
    st.title('Heart Disease Prediction System Using ML')
    
    
    # getting the input data from the user
    #column for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Cheest Pain Type')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('serum cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('fasting blood sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('resting electrocardiographic results (values 0,1,2)')
        
    with col2:
        thalach = st.text_input('maximum heart rate achieved')
        
    with col3:
        exang = st.text_input('exercise induced angina')
        
    with col1:
        oldpeak = st.text_input('oldpeak = ST depression induced by exercise relative to rest')
        
    with col2:
        slope = st.text_input('the slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        diab_diagnosis = hearts_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (diab_diagnosis[0] == 1):
            diab_diagnosis = 'The Person has Heart Disease'
            
        else:
            diab_diagnosis = 'The Person does not have a heart Disease'
            
    st.success(diab_diagnosis)


















