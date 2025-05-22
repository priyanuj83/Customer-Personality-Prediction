{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b3b3adc0-4443-44ed-8e6f-b8d7930169fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-21 21:00:32.922 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Priyanuj\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-05-21 21:00:32.925 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "# Load trained model\n",
    "model = joblib.load(\"best_logistic_model.pkl\")\n",
    "\n",
    "st.set_page_config(page_title=\"Customer Persona Predictor\", layout=\"centered\")\n",
    "st.title(\"🔮 Customer Persona Prediction App\")\n",
    "st.markdown(\"\"\"\n",
    "Welcome to the **Customer Persona Predictor**! \n",
    "Fill in the customer details below and click **Predict Persona** to find out which segment they belong to.\n",
    "\"\"\")\n",
    "\n",
    "# Input columns\n",
    "with st.form(\"persona_form\"):\n",
    "    col1, col2 = st.columns(2)\n",
    "\n",
    "    with col1:\n",
    "        year_birth = st.slider(\"Year of Birth\", 1940, 2005, 1980)\n",
    "        income = st.number_input(\"Yearly Income ($)\", min_value=1000, max_value=200000, value=50000)\n",
    "        kidhome = st.slider(\"Number of Kids at Home\", 0, 3, 0)\n",
    "        teenhome = st.slider(\"Number of Teenagers at Home\", 0, 3, 0)\n",
    "        recency = st.slider(\"Recency (Days since last purchase)\", 0, 100, 30)\n",
    "        customer_tenure = st.slider(\"Customer Tenure (Days)\", 0, 1000, 300)\n",
    "\n",
    "    with col2:\n",
    "        mnt_wines = st.slider(\"Amount Spent on Wines\", 0, 1500, 200)\n",
    "        mnt_meat = st.slider(\"Amount Spent on Meat\", 0, 1000, 150)\n",
    "        mnt_gold = st.slider(\"Amount Spent on Gold Products\", 0, 1000, 50)\n",
    "        num_web_purchases = st.slider(\"Web Purchases\", 0, 20, 5)\n",
    "        num_catalog_purchases = st.slider(\"Catalog Purchases\", 0, 20, 2)\n",
    "        num_store_purchases = st.slider(\"Store Purchases\", 0, 20, 4)\n",
    "\n",
    "    st.markdown(\"### Demographics\")\n",
    "    education = st.selectbox(\"Education Level\", [\"Basic\", \"2n Cycle\", \"Graduation\", \"Master\", \"PhD\"])\n",
    "    marital_status = st.selectbox(\"Marital Status\", [\"Single\", \"Married\", \"Together\", \"Divorced\", \"Widow\"])\n",
    "\n",
    "    submitted = st.form_submit_button(\"Predict Persona\")\n",
    "\n",
    "if submitted:\n",
    "    # Map categorical inputs (must match model training)\n",
    "    education_map = {\"Basic\": 0, \"2n Cycle\": 1, \"Graduation\": 2, \"Master\": 3, \"PhD\": 4}\n",
    "    marital_status_map = {\"Single\": [1, 0, 0, 0, 0], \"Married\": [0, 1, 0, 0, 0],\n",
    "                          \"Together\": [0, 0, 1, 0, 0], \"Divorced\": [0, 0, 0, 1, 0], \"Widow\": [0, 0, 0, 0, 1]}\n",
    "\n",
    "    education_encoded = education_map[education]\n",
    "    marital_encoded = marital_status_map[marital_status]\n",
    "\n",
    "    # Construct input feature vector (update this order to match training)\n",
    "    input_data = np.array([[\n",
    "        year_birth, education_encoded, income, kidhome, teenhome, recency,\n",
    "        mnt_wines, 0, mnt_meat, 0, 0, mnt_gold, 0, num_web_purchases, num_catalog_purchases,\n",
    "        num_store_purchases, 0, 0, 0, 0, 0, 0, 0, 0,\n",
    "        customer_tenure\n",
    "    ] + marital_encoded])\n",
    "\n",
    "    # Predict\n",
    "    predicted_cluster = model.predict(input_data)[0]\n",
    "\n",
    "    # Display Result\n",
    "    st.success(f\"🧠 Predicted Customer Segment (Cluster): **{predicted_cluster}**\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74a12a0d-ef02-4bfa-8871-7ad89772f34f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
