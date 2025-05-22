# 🧠 Customer Personality Prediction App

In this project we used **unsupervised clustering** and **supervised learning** to deliver intelligent, actionable insights for marketing teams. This interactive web app predicts customer personas based on their demographics and spending behavior, helping marketers drive personalized campaigns and optimize strategies.

## 🚀 Project Overview

In this project, we:
- Analyzed customer data from a marketing campaign dataset
- Clustered customers based on behavioral traits using **KMeans clustering**
- Labeled these clusters into meaningful **customer personas**
- Built a **prediction pipeline** using supervised ML models to classify new customers into personas
- Deployed a **Streamlit app** for real-time persona prediction

---

## 📊 Dataset

- **Source:** [marketing_campaign.csv](./marketing_campaign.csv)
- **Size:** 2240 records × 29 features
- **Features:** Demographics, purchasing patterns, campaign responses

Key features include:
- `Income`, `Education`, `Marital_Status`, `Year_Birth`, `Customer_Tenure`
- Product spends: `MntWines`, `MntMeatProducts`, `MntFishProducts`, etc.
- Campaign responses: `AcceptedCmp1` to `AcceptedCmp5`, `Response`

---

## 🔍 Unsupervised Learning: Customer Segmentation

We applied **KMeans clustering** on scaled numerical features to uncover hidden customer segments. The **Elbow Method** was used to determine the optimal number of clusters (k = 5).

### Identified Customer Segments:
1. **High Income Niche Spenders**
2. **Low Income Bargain Visitors**
3. **Mid Income Catalogue Buyers**
4. **Lowest Income Disengaged Users**
5. **Highest Income Premium Loyalists**

These clusters were later **labeled and mapped** to create our target variable for supervised learning.

---

## 🤖 Supervised Learning: Persona Prediction

Using the cluster labels as target classes, we trained multiple models to predict the customer persona:

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | 98.4%    |
| SVM (Linear)        | 98.4%    |
| XGBoost Classifier  | 95.0%    |
| Random Forest       | 94.2%    |

The best performing model was **Logistic Regression**, which we selected for deployment.

Hyperparameter tuning was done via `GridSearchCV`.

---

## 📌 Feature Importance

Using Random Forest and XGBoost, we identified key features driving customer segmentation:

- `Marital_Status_Single`
- `AcceptedCmp5` (last campaign success)
- `MntWines`, `MntMeatProducts`, `Income`
- `NumCatalogPurchases`

---

## 🛠️ Tech Stack

- **Python** (Pandas, Scikit-learn, XGBoost, Joblib)
- **Machine Learning**: KMeans, Logistic Regression, SVM, Random Forest, XGBoost
- **Deployment**: Streamlit
- **Visualization**: Matplotlib, Seaborn
- **Model Serialization**: Joblib

---

## 🌐 Streamlit App Demo

📍 [Click here to access the live app](https://customer-personality-prediction-kwzmh9ipezuhqkhwpfownr.streamlit.app/)

> Predict customer personas on the fly using a friendly interface!  
> Input features such as age, income, and purchase behavior and get real-time persona prediction.

