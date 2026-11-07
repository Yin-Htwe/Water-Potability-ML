import streamlit as st
import pickle
import pandas as pd

st.header("Water Potability Prediction App")

with open("./ML_Model/water_potability_model.pkl", "rb") as f:
    model = pickle.load(f)

with st.sidebar:
    st.header("ML Project")
    st.text("Project: Water Potability")
    st.text("Model: SVM")
    st.text("Class: Machine Learning")

col1, col2 = st.columns(2)

with col1:
    ph = st.number_input(
        "pH", min_value=0.0, max_value=14.0, value=7.0
    )

    hardness = st.number_input(
        "Hardness", min_value=0.0, value=196.0
    )

    solids = st.number_input(
        "Solids", min_value=0.0, value=20000.0
    )

    chloramines = st.number_input(
        "Chloramines", min_value=0.0, value=7.0
    )

    sulfate = st.number_input(
        "Sulfate", min_value=0.0, value=330.0
    )

with col2:
    conductivity = st.number_input(
        "Conductivity", min_value=0.0, value=425.0
    )

    organic_carbon = st.number_input(
        "Organic Carbon", min_value=0.0, value=14.0
    )

    trihalomethanes = st.number_input(
        "Trihalomethanes", min_value=0.0, value=66.0
    )

    turbidity = st.number_input(
        "Turbidity", min_value=0.0, value=4.0
    )

if st.button("Predict Water Potability"):

    input_data = pd.DataFrame([{
        "ph": ph,
        "Hardness": hardness,
        "Solids": solids,
        "Chloramines": chloramines,
        "Sulfate": sulfate,
        "Conductivity": conductivity,
        "Organic_carbon": organic_carbon,
        "Trihalomethanes": trihalomethanes,
        "Turbidity": turbidity
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Prediction: Potable Water")
        st.markdown("### 💦 Predicted as Drinkable Water")
        st.balloons()
    else:
        st.error("Prediction: Not Potable Water")
        st.markdown("### 🚫🥤 Predicted as Not Drinkable Water")

st.caption("For educational use only. Not a drinking-water safety test.")