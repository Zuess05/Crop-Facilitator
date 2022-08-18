import streamlit as st 
import pickle
import numpy as np

def load_fert():
    with open('saved_steps_fert.pkl','rb') as file:
        fer = pickle.load(file)
    return fer

f = load_fert()
mod = f['fert']
le = f['le']

def fert_price():
    soil_types_list = ['Sandy', 'Loamy', 'Black', 'Red', 'Clayey']
    crops_list = ['Maize', 'Sugarcane', 'Cotton', 'Tobacco', 'Paddy', 'Barley',
       'Wheat', 'Millets', 'Oil seeds', 'Pulses', 'Ground Nuts']
    st.title("Fertilizer Recommendation")
    st.write('Enter the following information')
    t = st.slider("Enter the average temperature in your area",-10,70,22)
    h = st.number_input("Enter the Humidity in your area")
    m = st.number_input("Enter the moisture content present in the soil")
    soil_type  = st.selectbox("Soil type",soil_types_list)
    crop = st.selectbox("Crop",crops_list)
    n = st.number_input("Enter the nitrogen content")
    k = st.number_input("Enter the potassium content")
    p = st.number_input("Enter the phosphorous content")

    fert_result = st.button('Predict the fertilizer')
    if fert_result:
        X = np.array([[t,h,m,soil_type,crop,n,k,p]])
        X[:,3] = le.fit_transform(X[:,3])
        X[:,4] = le.fit_transform(X[:,4])
        calc = mod.predict(X)
        st.subheader(f'The fertilizer to be used is {calc[0]}')

   