import streamlit as st
import joblib
import numpy as np
import seaborn as sns


model = joblib.load("model.pkl")


st.title("House Price Prediction App")

st.divider()
st.write("This app uses machine learning to predicting houses prices in India given features of the house. To use this app, you can enter the inputs from this user interface and then use 'predict' button")


st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value = 0, value = 0)
bathrooms = st.number_input("Number of Bathrooms", min_value = 0, value = 0)
livingarea = st.number_input("Living Area", min_value  = 0, value = 2000)
condition = st.number_input("Condition of House", min_value=0, value=3)
numberofschools = st.number_input("Number of Schools Nearby ", min_value=0, value=0)



st.divider()

x = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]

predictbutton= st.button("Predict")

if predictbutton:

    st.balloons()

    x_array = np.array(x)

    prediction = model.predict(x_array)[0]

    st.write(f"Price prediction is ${prediction:,.2f}")

else:
    st.write("Please use predict button after entering values.")


