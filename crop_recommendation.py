import streamlit as st
import pickle

def load_crop_recom():
    with open('saved_steps_recom.pkl','rb') as file:
        mod = pickle.load(file)
    return mod

dt = load_crop_recom()
model = dt['dt']

def predict_crop_recom():
    st.title("Crop Recommender")
    st.write('Enter the following information')
    n = st.number_input("Enter the nitrogen content present in the soil")
    p = st.number_input("Enter the Phosphorous content present in the soil")
    k = st.number_input("Enter the Potassium content present in the soil")
    ph = st.number_input("Enter the pH content of the soil")
    t = st.slider("Enter the average temperature in your area",-10,70,22)
    h = st.number_input("Enter the percentage of average humidity in your area")
    r = st.number_input("Enter the average rainfall in our area")
    X = [[n,p,k,t,h,ph,r]] 
    result = model.predict(X)
    st.subheader(f"The crop you can think of growing is {result[0]}")