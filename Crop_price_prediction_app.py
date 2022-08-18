import streamlit as st
from predict_page import predict
from crop_recommendation import predict_crop_recom
from fert_prediction import fert_price

page = st.sidebar.selectbox("More Options: ", ("Crop Price prediction",'Crop Recommendation','Fertilizer Recommendation'))

with open('style.css') as f :
    st.markdown(f'<style> {f.read()} </style>', unsafe_allow_html = True)

if page == "Crop Price prediction":
    predict()
elif page=='Crop Recommendation':
    predict_crop_recom()
else:
    fert_price()