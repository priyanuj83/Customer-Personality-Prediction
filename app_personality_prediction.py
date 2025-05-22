import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load("best_logistic_model.pkl")

st.set_page_config(page_title="Customer Persona Predictor", layout="centered")
st.title("🔮 Customer Persona Prediction App")
st.markdown("""
Welcome to the **Customer Persona Predictor**! 
Fill in the customer details below and click **Predict Persona** to find out which segment they belong to.
""")

# Input columns
with st.form("persona_form"):
    col1, col2 = st.columns(2)

    with col1:
        year_birth = st.slider("Year of Birth", 1940, 2005, 1980)
        income = st.number_input("Yearly Income ($)", min_value=1000, max_value=200000, value=50000)
        kidhome = st.slider("Number of Kids at Home", 0, 3, 0)
        teenhome = st.slider("Number of Teenagers at Home", 0, 3, 0)
        recency = st.slider("Recency (Days since last purchase)", 0, 100, 30)
        customer_tenure = st.slider("Customer Tenure (Days)", 0, 1000, 300)

    with col2:
        mnt_wines = st.slider("Amount Spent on Wines", 0, 1500, 200)
        mnt_meat = st.slider("Amount Spent on Meat", 0, 1000, 150)
        mnt_gold = st.slider("Amount Spent on Gold Products", 0, 1000, 50)
        num_web_purchases = st.slider("Web Purchases", 0, 20, 5)
        num_catalog_purchases = st.slider("Catalog Purchases", 0, 20, 2)
        num_store_purchases = st.slider("Store Purchases", 0, 20, 4)

    st.markdown("### Demographics")
    education = st.selectbox("Education Level", ["Basic", "2n Cycle", "Graduation", "Master", "PhD"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Together", "Divorced", "Widow"])

    submitted = st.form_submit_button("Predict Persona")

if submitted:
    # Map categorical inputs (must match model training)
    education_map = {"Basic": 0, "2n Cycle": 1, "Graduation": 2, "Master": 3, "PhD": 4}
    marital_status_map = {"Single": [1, 0, 0, 0, 0], "Married": [0, 1, 0, 0, 0],
                          "Together": [0, 0, 1, 0, 0], "Divorced": [0, 0, 0, 1, 0], "Widow": [0, 0, 0, 0, 1]}

    education_encoded = education_map[education]
    marital_encoded = marital_status_map[marital_status]

    # Construct input feature vector (update this order to match training)
    input_data = np.array([[
        year_birth, education_encoded, income, kidhome, teenhome, recency,
        mnt_wines, 0, mnt_meat, 0, 0, mnt_gold, 0, num_web_purchases, num_catalog_purchases,
        num_store_purchases, 0, 0, 0, 0, 0, 0, 0, 0,
        customer_tenure
    ] + marital_encoded])

    # Predict
    predicted_cluster = model.predict(input_data)[0]

    # Map cluster number to descriptive label
    cluster_label_map = {
        0: "Low Income Bargain Visitor",
        1: "Highest Income Premium Loyalists",
        2: "Lowest Income Disengaged Users",
        3: "Mid Income Catalogue Buyers",
        4: "High Income Niche Spenders"
}

    predicted_label = cluster_label_map.get(predicted_cluster, "Unknown")

    # Display Result
    st.success(f"🧠 Predicted Customer Segment: **{predicted_label}** (Cluster {predicted_cluster})")
