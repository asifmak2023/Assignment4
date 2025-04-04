import streamlit as st
import pandas as pd

st.title("Body Mass Index Calculator")

weight = st.slider("Enter your weight in kilograms",50,250,110,10)
height = st.slider("Enter your height in meters",1.5,2.0,1.7,0.1)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is {bmi:.2f}")